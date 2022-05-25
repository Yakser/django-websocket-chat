from django.forms.widgets import ClearableFileInput, CheckboxSelectMultiple


class CustomClearableFileInput(ClearableFileInput):
    template_name = 'includes/clearable_file_input.html'


class CustomCheckboxSelectMultiple(CheckboxSelectMultiple):
    template_name = 'includes/checkbox_select.html'
