import json, bcrypt

from django.http.response   import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from .models                import User
from .validation            import signup_password, signup_email

class SignUpView(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            name         = data["name"]
            email        = data['email']
            password     = data["password"]
            phone        = data["phone"]

            signup_email(email)

            signup_password(password)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message" : "EMAIL_ALREADY_EXISTS"}, status=400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                name     = name,
                email    = email,
                passwd   = hashed_password,
                phone    = phone
                )

            return JsonResponse({"message": "Success"}, status = 201)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except ValidationError as e:
            return JsonResponse({"message": e.message}, status=400)

class LogInView(View):
    def post(self, request):
        try:
            data      = json.loads(request.body)
            email     = data["email"]
            password  = data["password"]

            if not User.objects.filter(email=email, password=password).exists():
                return JsonResponse({"message":"INVALID_USER"}, status=400)

            return JsonResponse({"message" : "SUCCESS"}, status=200)

        except KeyError:
              return JsonResponse({"message" : "KEY_ERROR"}, status=400)
