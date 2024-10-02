from django.forms import ModelForm
from django import forms
from .models import *

class ChatMessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widget = {
            'body': forms.TextInput(attrs={'placeholder': 'Escriba un mensaje...', 'class': 'p-4 text-black', 'max-length': '240', 'autofocus':True})
        }