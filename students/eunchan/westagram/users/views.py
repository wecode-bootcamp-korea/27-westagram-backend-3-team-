import json, bcrypt

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

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
            data         = json.loads(request.body) 
            email        = data["email"]
            password     = data["password"]	
        
            if not Member.objects.filter(email=email, password=password).exists():
                return JsonResponse({'massage': "INVALID_USER" }, status=401)
            
            return JsonResponse({'massage':"SUCCESS"}, status=200)
        
        except KeyError :
            return JsonResponse({'massage':"KEY_ERROR"}, status=400)
