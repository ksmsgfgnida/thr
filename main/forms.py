from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Performance, User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

# остальной код вашего файла forms.py


class LoginForm(AuthenticationForm):
# Добавьте дополнительные поля, если нужно
    pass

class RegistrationForm(UserCreationForm):
# Добавьте дополнительные поля, если нужно, например, email
    email = forms.EmailField()

class Meta:
    model = User
    fields = UserCreationForm.Meta.fields + ('email',)


class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = '__all__'  # Include all fields from the Performance model