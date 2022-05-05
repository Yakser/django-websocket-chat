from django.views.generic.base import TemplateView
from websockets.connection_types import USERS_CHANNELS_CONNECTION


class UsersChannelsView(TemplateView):
    template_name = 'users_channels/users_channels.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['connection_type'] = USERS_CHANNELS_CONNECTION
        return context
