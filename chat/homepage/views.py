from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    """
    Отображает главную страницу

    Template:
        template_name: 'homepage/home.html'

    """
    template_name = 'homepage/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
