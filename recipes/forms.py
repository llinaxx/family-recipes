from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'category', 'author', 'cooking_time', 'ingredients', 'instructions', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название блюда'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'cooking_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    # КАСТОМНАЯ ВАЛИДАЦИЯ (требование методички)
    def clean_cooking_time(self):
        cooking_time = self.cleaned_data.get('cooking_time')
        if cooking_time < 5:
            raise forms.ValidationError("Время готовки не может быть меньше 5 минут!")
        return cooking_time
