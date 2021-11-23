import json, re

from django.core.exceptions           import ValidationError

from users.models                     import User
from django.http                      import JsonResponse

data     = json.loads(request.body)
name     = data["name"]
email    = data["email"]
password = data["password"]
contact  = data["contact"]

# def Validation_Email(email):

#     email_validation    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
#     if not re.match(email_validation, email):
#         raise ValidationError("Email_Invalidation")

#     if User.objects.filter(email = email).exists():    #형식이 맞는지가 우선? 등록 된사람이 우선? return은 왜 안됨? 공백, !=, not
#         raise ValidationError("User_Already_Exists")   #이메일의 정규표현식을 거르고, 등록된 사람인지 체크하고, 비밀번호 체크???


# def Validation_Password(password):

#     password_validation = '(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%*^&+=])([a-zA-Z0-9!@#$%*^&+=]{8,})'

#     if not re.match(password_validation, password):
#         raise ValidationError("PassWord_Invalidation")


def validation_e(email):
    def val_decorator(test):
        email_validation    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_validation, email):
            raise ValidationError("Email_Invalidation")
        return test
    return val_decorator

@validation_e
def test():
    User.objects.create(
            name     = name,
            email    = email,
            password = password,
            contact  = contact
        )


