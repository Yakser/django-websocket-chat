from django.views.generic.base import TemplateView


class UsersChannelsView(TemplateView):
    template_name = 'users_channels/users_channels.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
