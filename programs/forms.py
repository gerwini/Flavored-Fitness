from django import forms
from .widgets import CustomClearableFileInput
from .models import Program


class ProgramForm(forms.ModelForm):  # Form for the programs

    class Meta:
        model = Program
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

