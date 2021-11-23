import json

from django.http                import JsonResponse
from django.views               import View
from django.core.exceptions     import ValidationError

from users.models               import User
from users.validation           import validation_email, validation_password


class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            if not User.objects.filter(email = data["email"], password = data["password"]).exists():
                return JsonResponse({'message':'INVALID_USER'}, status = 401)
            return JsonResponse({'message':'SUCCESS'},status = 200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status = 400)


class SignUpView(View):
    def post(self, request):
      
        try:
            data     = json.loads(request.body)
            name     = data["name"]
            email    = data["email"]
            password = data["password"]
            contact  = data["contact"]
           
            validation_email(email)
            validation_password(password)
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({"MESSAGE":"User_Already_Exists"}, status = 400)

            User.objects.create(
                name     = name,
                email    = email,
                password = password,
                contact  = contact
            )

            return JsonResponse({"MESSAGE":"SUCCESS"}, status = 201)
        
        except ValidationError as e:
            return JsonResponse({"MESSAGE":e.message}, status = 400)

        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status = 400)