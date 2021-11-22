import json, re

from django.http      import JsonResponse
from django.views     import View
from users.models     import User

class SignInView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            password = User.objects.get(email = data["email"]).password
            
            if not data['password'] == password:
                return JsonResponse({'message':'INVALID_USER'}, status = 400)
            return JsonResponse({'message':'SUCCESS'},status = 200)
        
        except User.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_USER'}, status = 401)

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

            email_validation    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            password_validation = '(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%*^&+=])([a-zA-Z0-9!@#$%*^&+=]{8,})'
            
            if not re.match(email_validation, email):
                return JsonResponse({"MESSAGE":"Email_Error"}, status = 400)

            if not re.match(password_validation, password):
                return JsonResponse({"MESSAGE":"Password_Error"}, status = 400)

            if User.objects.filter(email = email).exists():
                return JsonResponse({"MESSAGE":"User_Already_Exists"}, status = 400)  
            
            User.objects.create(
                name     = name,
                email    = email,
                password = password,
                contact  = contact
            )

            return JsonResponse({"MESSAGE":"SUCCESS"}, status = 201)

        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status = 400)