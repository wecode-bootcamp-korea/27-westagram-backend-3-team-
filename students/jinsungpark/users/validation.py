import re

from django.core.exceptions import ValidationError

from .models                import User

def Signup_email(email):
    email_regex  = '^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$'
    if User.objects.filter(email=email).exists():
        raise ValidationError("EMAIL_ALREADY_EXISTS")

    if not re.match(email_regex, email):
        raise ValidationError("EMAIL_ERROR")

def Signup_password(password):
    passwd_regex = '^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$'
    if not re.match(passwd_regex, password):
        raise ValidationError("PASSWORD_ERROR")

def Log_in(email, password):
    user = User.objects.get(email=email)

    if user.passwd != password:
        raise ValidationError('INVALID_USER')


