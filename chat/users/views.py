from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from users.forms import EditProfileForm, SignupForm

User = get_user_model()


class UserListView(TemplateView):
    template_name = 'users/user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.only('id', 'username')
        context['users'] = users
        return context


class UserDetailView(TemplateView):
    template_name = 'users/user_detail.html'

    def get_context_data(self, id, **kwargs):
        context = super().get_context_data(**kwargs)

        user = get_object_or_404(User.objects.only('email', 'username'), pk=id)
        context['user'] = user

        return context


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'users/profile.html'
    form_class = EditProfileForm

    def get(self, request, *args, **kwargs):
        return render(request,
                      self.template_name,
                      self.get_context_data(request))

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User.objects.only('email', 'username'),
                                 pk=request.user.id)

        form = self.form_class(request.POST, request.FILES)

        if form.is_valid() and form.validate_all(request.user):
            user.email = form.cleaned_data['email']
            user.username = form.cleaned_data['login']
            user.profile.biography = form.cleaned_data['biography'] or user.profile.biography

            # if clear image checkbox is checked
            if form.cleaned_data['image'] is False:
                user.profile.image = None
            else:
                user.profile.image = form.cleaned_data['image'] or user.profile.image

            user.save()

            return redirect('users:profile')

        return render(request,
                      self.template_name,
                      self.get_context_data(request))

    def get_context_data(self, request, **kwargs):
        context = super().get_context_data(**kwargs)

        user = get_object_or_404(User.objects.only('email', 'username'),
                                 pk=request.user.id)

        form = self.form_class(request.POST or None,
                               request.FILES or None,
                               initial={'email': user.email,
                                        'login': user.username,
                                        'biography': user.profile.biography,
                                        'image': user.profile.image
                                        })

        context['user'] = user
        context['form'] = form

        return context


class SignupView(TemplateView):
    template_name = 'users/signup.html'
    form_class = SignupForm

    def get(self, request, *args, **kwargs):
        return render(request,
                      self.template_name,
                      self.get_context_data(request))

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(request)

        form = context['form']

        if form.is_valid() and form.check_passwords_match():
            user = User.objects.create_user(
                username=form.cleaned_data['login'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
            )

            login(request, user)

            return redirect('homepage:home')

        return render(request,
                      self.template_name,
                      self.get_context_data(request))

    def get_context_data(self, request, **kwargs):
        context = super().get_context_data(**kwargs)

        form = self.form_class(request.POST or None)
        context['form'] = form

        return context
