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
    template_name = 'groups/group.html'

    def get(self, request, group_slug: str, *args, **kwargs):
        return render(request,
                      self.template_name,
                      self.get_context_data(request.user, group_slug))

    def get_context_data(self, user: User, group_slug: str, **kwargs):
        context = super().get_context_data(**kwargs)

        group: Group = get_object_or_404(Group, slug=group_slug)

        if group.group_members.filter(id=user.id):
            container, created = DailyGroupMessages.objects.get_or_create(group=group)

            prefetch_users = Prefetch('user', queryset=User.objects.only('username'))
            messages = container.group_messages.prefetch_related(prefetch_users)

            context['is_member'] = True
            context['group'] = group
            context['messages'] = messages
        else:
            context['is_member'] = False

        context['connection_type'] = GROUPS_CONNECTION
        context['user'] = user

        return context


@method_decorator(login_required, name='dispatch')
class CreateGroupView(TemplateView):
    template_name = 'groups/create_group.html'
    form_class = CreateGroupForm

    def get(self, request, *args, **kwargs):
        return render(request,
                      self.template_name,
                      self.get_context_data(request.user.id))

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User.objects.all(),
                                 pk=request.user.id)

        form = self.form_class(request.POST, user=user)

        if form.is_valid():
            members: QuerySet = form.cleaned_data['group_members']

            group = Group(slug=form.cleaned_data['slug'],
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

        user = get_object_or_404(User.objects.only('email', 'username'),
                                 pk=id)

        form = self.form_class(user=user)

        context['user'] = user
        context['form'] = form

        return context


@method_decorator(staff_member_required, name='dispatch')
class GroupsListView(TemplateView):
    template_name = 'groups/groups_list.html'

    def get(self, request, *args, **kwargs):
        return render(request,
                      self.template_name,
                      self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        groups = Group.objects.only('slug', 'name')

        context['groups'] = groups

        return context


@method_decorator(login_required, name='dispatch')
class ClearGroupMessagesConfirmView(TemplateView):
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
class EditGroupView(TemplateView):
    template_name = 'groups/edit_group.html'
    form_class = EditGroupForm

    def get(self, request, group_slug: str, *args, **kwargs):
        return render(request,
                      self.template_name,
                      self.get_context_data(request, group_slug))

    def post(self, request, group_slug: str, *args, **kwargs):
        group = get_object_or_404(Group.objects.all(),
                                  pk=group_slug)
        user = get_object_or_404(User.objects.only('id'),
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

        form = self.form_class(request.POST or None,
                               request.FILES or None,
                               user=user,
                               initial={
                                   'name': group.name,
                                #    'group_members': group.group_members,
                                   'image': group.image,
                               })

        # небоходимо, чтобы показать ошибки
        if form.is_valid():
            form.validate_all(group)

        context['group'] = group
        context['form'] = form

        return context
