import re

from django.core.exceptions import ValidationError

def Signup_email(email):
    email_regex  = '^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$'

    if not re.match(email_regex, email):
        raise ValidationError("EMAIL_ERROR")

def Signup_password(password):
    passwd_regex = '^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$'
    
    if not re.match(passwd_regex, password):
        raise ValidationError("PASSWORD_ERROR")



