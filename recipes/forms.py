from django import forms
from .widgets import CustomClearableFileInput
from .models import Recipe


class RecipeForm(forms.ModelForm):  # Form for adding and editing the model

    class Meta:
        model = Recipe
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

