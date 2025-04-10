# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from .models import *

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'importance', 'estimated_minutes']



class Task_highform(forms.ModelForm):
    class Meta:
        model = Task_high
        fields = ['title', 'description', 'due_date', 'estimated_minutes', 'status', 'importance', 'repeat_interval']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Add some details...',
            }),
            'due_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
            }),
            'estimated_minutes': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Estimated time in minutes',
                'min': 1,
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
            'importance': forms.Select(attrs={
                'class': 'form-control',
            }),
            'repeat_interval': forms.Select(attrs={
                'class': 'form-control',
            }),
        }


class Task_mediumform(forms.ModelForm):
    class Meta:
        model = Task_medium
        fields = ['title', 'description', 'due_date', 'estimated_minutes', 'importance', 'category', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Optional description...',
            }),
            'due_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
            }),
            'estimated_minutes': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 45',
                'min': 1,
            }),
            'importance': forms.Select(attrs={
                'class': 'form-control',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
        }



class Task_lowform(forms.ModelForm):
    class Meta:
        model = Task_low
        fields = ['title','due_date','description' ,'importance','estimated_minutes']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Quick task title',
            }),
             'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Add some details...'
            }),
            'due_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
            }),
             'importance': forms.Select(attrs={
                'class': 'form-control',
            }),
            'estimated_minutes': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 45',
                'min': 1,
            }),
        }
