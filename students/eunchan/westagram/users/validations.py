import re

from django.core.exceptions import ValidationError

from users.models           import Member

def email_regexp_check(email):
    email_regexp    = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regexp, email): 
        raise ValidationError("INVALID_EMAIL_ADDRESS")

def password_regexp_check(password):
    password_regexp = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&(){}\[\]])[A-Za-z\d@$!%*#?&(){}\[\]]{8,}$"
    if not re.match(password_regexp , password):
        raise ValidationError("INVALID_PASSWORD")