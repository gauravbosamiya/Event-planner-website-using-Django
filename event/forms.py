from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password

from .models import User


class CustomUserCreateForm(UserCreationForm):

    class Meta:
        model = User
        help_texts = {
            'username': None,
        }

        fields = ['username', 'email', 'name', 'password1', 'password2']










