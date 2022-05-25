from django.views.generic.base import TemplateView


class AboutView(TemplateView):
    """
    Отображает страницу информации о проекте

    Template:
        template_name: 'info/about.html'

    """
    template_name = 'info/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InstructionView(TemplateView):
    """
    Отображает страницу с инструкцией по использованию

    Template:
        template_name: 'info/instruction.html'

    """
    
    template_name = 'info/instruction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context