from django.views.generic.base import TemplateView


class GroupsView(TemplateView):
    template_name = 'groups/group.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
