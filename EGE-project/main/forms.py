from .models import Files, Info
from django.forms import ModelForm, TextInput, EmailInput, FileInput


class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = ["email", "name"]
        widgets = {
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Адрес электронной почты"
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "ФИО"
            }),
        }


class FilesForm(ModelForm):
    class Meta:
        model = Files
        fields = ["title", "file"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите название"
            }),
            "file": FileInput(attrs={
                'class': "file-input",
                'placeholder': "Файл",
            }
            )
        }
