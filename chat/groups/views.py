from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from users_messages.models import DailyGroupMessages
from websockets.connection_types import GROUPS_CONNECTION

from groups.forms import CreateGroupForm, EditGroupForm
from groups.models import Group

User = get_user_model()


@method_decorator(login_required, name='dispatch')
class GroupView(TemplateView):
    """
    Отображает модель Group - список сообщений, панель редактирования и удаления группы,
    поле отправки сообщения

    Context:
        connection_type (str): тип подключения к вебсокетам
        is_member (bool): флаг, указывающий является ли пользователь участником группы
        user (User): экземпляр класса User
        group (Group): экземпляр класса Group
        messages (UserGroupMessage[]): сообщения группы
        members_count (int): количество участников групы

    Template:
        template_name: 'groups/group.html'

    """

    template_name = 'groups/group.html'

    def get(self, request, group_slug: str, *args, **kwargs):
        return render(request,
                      self.template_name,
                      self.get_context_data(request.user, group_slug))

    def get_context_data(self, user: User, group_slug: str, **kwargs):
        context = super().get_context_data(**kwargs)
        group: Group = get_object_or_404(Group, slug=group_slug)

        context['connection_type'] = GROUPS_CONNECTION
        context['user'] = user
        context['members_count'] = group.group_members.count()
        context['is_member'] = False

        if self._check_if_user_is_member(group, user):
            container, created = DailyGroupMessages.objects.get_or_create(group=group)

            prefetch_users = Prefetch('user', queryset=User.objects.only('username'))
            messages = container.group_messages.prefetch_related(prefetch_users)

            context['is_member'] = True
            context['group'] = group
            context['messages'] = messages

        return context

    def _check_if_user_is_member(self, group: Group, user: User) -> bool:
        return group.group_members.filter(id=user.id)


@method_decorator(login_required, name='dispatch')
class CreateGroupView(TemplateView):
    """
    Отображает форму создания группы

    Context:
        user (User): экземпляр класса User
        form (CreateGroupForm): форма создания группы

    Template:
        template_name: 'groups/create_group.html'

    Form:
        form_class: CreateGroupForm

    """

    template_name = 'groups/create_group.html'
    form_class = CreateGroupForm

    def get(self, request, *args, **kwargs):
        return render(request,
                      self.template_name,
                      self.get_context_data(request.user.id))

    def post(self, request, *args, **kwargs):
        user: User = get_object_or_404(User.objects.all(),
                                       pk=request.user.id)

        form = self.form_class(request.POST, user=user)

        if form.is_valid():
            members: QuerySet = form.cleaned_data['group_members']

            group: Group = Group(slug=form.cleaned_data['slug'],
                                 name=form.cleaned_data['name'],
                                 owner=user)
            group.save()
            group.group_members.set(members)
            group.group_members.add(user)
            group.save()

            return redirect('groups:group', form.cleaned_data['slug'])

        return self.get(request)

    def get_context_data(self, id, **kwargs):
        context = super().get_context_data(**kwargs)

        user: User = get_object_or_404(User.objects.only('email', 'username'),
                                       pk=id)
        form = self.form_class(user=user)

        context['user'] = user
        context['form'] = form

        return context


@method_decorator(staff_member_required, name='dispatch')
class GroupsListView(TemplateView):
    """
    Отображает список групп (Group)

    Context:
        groups (Group[]): QuerySet содержащий экземпляры класса Group

    Template:
        template_name: 'groups/groups_list.html'

    """

    template_name = 'groups/groups_list.html'

    def get(self, request, *args, **kwargs):
        return render(request,
                      self.template_name,
                      self.get_context_data(request.user))

    def get_context_data(self, user: User, **kwargs):
        context = super().get_context_data(**kwargs)
        groups = user.users_groups.all()
        context['groups'] = groups
        return context


@method_decorator(login_required, name='dispatch')
class ClearGroupMessagesConfirmView(TemplateView):
    """
    Отображает модальное окно с подтверждением удаления истории сообщений группы

    Context:
        group (Group): экземпляр класса Group

    Template:
        template_name: 'groups/clear_group_messages_confirm.html'

    """

    template_name = 'groups/clear_group_messages_confirm.html'

    def get(self, request, group_slug: str, *args, **kwargs):
        return render(request,
                      self.template_name,
                      self.get_context_data(group_slug))

    def get_context_data(self, group_slug: str, **kwargs):
        context = super().get_context_data(**kwargs)

        group = get_object_or_404(Group, pk=group_slug)

        context['group'] = group

        return context


@method_decorator(login_required, name='dispatch')
class ClearGroupMessagesView(TemplateView):
    """
    Отображает страницу с сообщением об успешном удалении истории сообщений группы

    Context:
        group (Group): экземпляр класса Group

    Template:
        template_name: 'groups/clear_group_messages.html'

    """

    template_name = 'groups/clear_group_messages.html'

    def get(self, request, group_slug: str, *args, **kwargs):
        group = get_object_or_404(Group, pk=group_slug)

        group_container = DailyGroupMessages.objects.get(group=group)
        group_container.group_messages.all().delete()

        return render(request,
                      self.template_name,
                      self.get_context_data(group_slug))

    def get_context_data(self, group_slug: str, **kwargs):
        context = super().get_context_data(**kwargs)

        group = get_object_or_404(Group, pk=group_slug)

        context['group'] = group

        return context


@method_decorator(login_required, name='dispatch')
class DeleteGroupView(TemplateView):
    template_name = 'groups/delete_group_messages.html'

    def get(self, request, group_slug: str, *args, **kwargs):
        group = get_object_or_404(Group, pk=group_slug)

        group_container = DailyGroupMessages.objects.get(group=group)
        group_container.group_messages.all().delete()

        group.delete()

        return render(request,
                      self.template_name,
                      self.get_context_data(group_slug))

    def get_context_data(self, group_slug: str, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


@method_decorator(login_required, name='dispatch')
class EditGroupView(TemplateView):
    """
    Отображает страницу с сообщением об успешном удалении истории сообщений группы

    Context:
        group (Group): экземпляр класса Group
        form (EditGroupForm): форма редактирования группы

    Template:
        template_name: 'groups/edit_group.html'

    Form:
        form_class (EditGroupForm): форма редактирования группы

    """

    template_name = 'groups/edit_group.html'
    form_class = EditGroupForm

    def get(self, request, group_slug: str, *args, **kwargs):
        return render(request,
                      self.template_name,
                      self.get_context_data(request, group_slug))

    def post(self, request, group_slug: str, *args, **kwargs):
        group: Group = get_object_or_404(Group.objects.all(),
                                         pk=group_slug)

        if request.POST.get('delete') != None:
            # group.delete()
            # return redirect('/groups/edit/g1/')
            # return render(request, 'groups/delete_group_messages.html')
            pass
    
        user: User = get_object_or_404(User.objects.only('id'),
                                       pk=request.user.id)

        form = self.form_class(request.POST, request.FILES, user=user)

        if form.is_valid() and group.owner == user:
            group.name = form.cleaned_data['name']

            members: QuerySet = form.cleaned_data['group_members']

            if members:
                group.group_members.set(members)
                group.group_members.add(user)

            group.save()

            # if clear image checkbox is checked
            if form.cleaned_data['image'] is False:
                group.image = None
            else:
                group.image = form.cleaned_data['image'] or group.image

            group.save()

            return redirect('groups:group', group.slug)

        return render(request,
                      self.template_name,
                      self.get_context_data(request, group_slug))

    def get_context_data(self, request, group_slug: str, **kwargs):
        context = super().get_context_data(**kwargs)

        group = get_object_or_404(Group.objects.all(),
                                  pk=group_slug)
        user = get_object_or_404(User.objects.only('id'),
                                 pk=request.user.id)

        initial_form_data = {
            'name': group.name,
            'group_members': group.group_members.all,
            'image': group.image,
        }

        form = self.form_class(request.POST or None,
                               request.FILES or None,
                               user=user,
                               initial=initial_form_data)

        # небоходимо, чтобы показать ошибки валидации формы
        if form.is_valid():
            form.validate_all(group)

        context['group'] = group
        context['form'] = form
        context['edit'] = True

        return context
