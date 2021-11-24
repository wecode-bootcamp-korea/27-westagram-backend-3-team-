import json, bcrypt, jwt

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from my_settings            import SECRET_KEY 
from users.models           import Member
from users.validations      import email_regexp_check, password_regexp_check

class SignupView(View):
    def post(self, request):
        try:
            data            = json.loads(request.body) 
            name            = data["name"]
            email           = data["email"]
            password        = data["password"]
            phone_number    = data["phone_number"]
            information     = data.get("information")

            email_regexp_check(email)
            password_regexp_check(password)

            if Member.objects.filter(email=email).exists():
                raise ValidationError("EMAIL DUPLICATE")

            hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')

            Member.objects.create(
                name         = name,
                email        = email,
                password     = hashed_password,
                phone_number = phone_number,
                information  = information
            )
            return JsonResponse({'massage':"SUCCESS"}, status=201)

        except KeyError :
            return JsonResponse({'massage':"KEY_ERROR"}, status=400)

        except ValidationError as e:
            return JsonResponse({'massage': e.message}, status=400)

class LoginView(View):
    def post(self, request):
        try:
            data       = json.loads(request.body) 
            email      = data["email"]
            password   = data["password"]	
            account    = Member.objects.get(email=email)
            
            if not bcrypt.checkpw(password.encode('utf-8'),account.password.encode('utf-8')):
                raise Member.DoesNotExist

            access_token = jwt.encode({'id' : account.id}, SECRET_KEY, algorithm = 'HS256')
            return JsonResponse({'token':access_token}, status=200)

        except Member.DoesNotExist :
            return JsonResponse({'massage':"INVALID_USER"}, status=401)

        except KeyError :
            return JsonResponse({'massage':"KEY_ERROR"}, status=400)
