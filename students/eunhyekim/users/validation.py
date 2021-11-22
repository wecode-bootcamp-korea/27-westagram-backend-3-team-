import re

from django.core.exceptions           import ValidationError

from users.models                     import User

def Validation_Email(email):

    email_validation    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if User.objects.filter(email = email).exists():
        raise ValidationError("User_Already_Exists")

    if not re.match(email_validation, email):
        raise ValidationError("Email_Invalidation")

def Validation_Password(password):

    password_validation = '(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%*^&+=])([a-zA-Z0-9!@#$%*^&+=]{8,})'

    if not re.match(password_validation, password):
        raise ValidationError("PassWord_Invalidation")
