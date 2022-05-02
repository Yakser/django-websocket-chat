from django.views.generic.base import TemplateView


class AboutView(TemplateView):
    template_name = 'info/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InstroctionView(TemplateView):
    template_name = 'info/instruction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context