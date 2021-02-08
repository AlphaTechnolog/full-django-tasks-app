from django import forms
from django.contrib.auth.models import User
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'completed', 'user']
        widgets = {
            'completed': forms.HiddenInput(),
            'user': forms.HiddenInput()
        }

class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'completed', 'user']
        widgets = {
            'user': forms.HiddenInput(),
        }
