from django import forms
from .models import Vacancy

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = '__all__'
        exclude = ['views']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Elon nomini kiriting...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Elon haqida qisqacha maʼlumot...',
                'rows': 4
            }),
            'category': forms.Select(attrs={
                'class': 'form-select mb-3'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Telefon raqamini kiriting...'
            }),
            'salary': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Oylik maoshni kiriting...'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control mb-3'
            }),
            'video': forms.ClearableFileInput(attrs={
                'class': 'form-control mb-3'
            }),
            'published': forms.CheckboxInput(attrs={
                'class': 'form-check-input mb-3'
            }),
        }


