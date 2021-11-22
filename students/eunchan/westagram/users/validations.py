import re

from django.core.exceptions import ValidationError

from users.models           import Member

email_regexp    = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
password_regexp = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&(){}\[\]])[A-Za-z\d@$!%*#?&(){}\[\]]{8,}$"

def signup_check(email, password):
            if Member.objects.filter(email=email).exists():
                raise ValidationError("EMAIL DUPLICATE")

            if not re.match(email_regexp, email): 
                raise ValidationError("INVALID_EMAIL_ADDRESS")

            if not re.match(password_regexp , password):
                raise ValidationError("INVALID_PASSWORD")


def login_check(email, password):
            if not re.match(email_regexp, email): 
                raise ValidationError("INVALID_EMAIL_ADDRESS")

            if not re.match(password_regexp , password):
                raise ValidationError("INVALID_PASSWORD")

            if Member.objects.get(email=email).password != password:
                raise Member.DoesNotExist		