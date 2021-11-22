import re

from django.core.exceptions           import ValidationError

from users.models                     import User


def Validation(email, password):

    email_validation    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    password_validation = '(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%*^&+=])([a-zA-Z0-9!@#$%*^&+=]{8,})'

    if User.objects.filter(email = email).exists():
        raise ValidationError("User_Already_Exists")

    if not re.match(email_validation, email):
        raise ValidationError("Email_Invalidation")

    if not re.match(password_validation, password):
        raise ValidationError("PassWord_Invalidation")
