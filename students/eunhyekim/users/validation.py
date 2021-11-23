import re

from django.core.exceptions           import ValidationError

def validation_email(email):

    email_validation    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if not re.match(email_validation, email):
        raise ValidationError("Email_Invalidation")

def validation_password(password):

    password_validation = '(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%*^&+=])([a-zA-Z0-9!@#$%*^&+=]{8,})'

    if not re.match(password_validation, password):
        raise ValidationError("PassWord_Invalidation")


