from django.forms.widgets import ClearableFileInput


class CustomClearableFileInput(ClearableFileInput):
    template_name = 'includes/clearable_file_input.html'
