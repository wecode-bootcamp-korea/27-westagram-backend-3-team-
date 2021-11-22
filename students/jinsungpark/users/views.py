import re, json

from django.http.response   import JsonResponse
from django.views           import View

from .models                import User

class SignUpView(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            name         = data["name"]
            email        = data['email']
            password     = data["password"]
            phone        = data["phone"]
            email_regex  = '^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$'
            passwd_regex = '^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$'

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message" : "EMAIL_ALREADY_EXISTS"}, status=400)

            if not re.match(email_regex, email):
                return JsonResponse({"message": "EMAIL_ERROR"}, status=400)

            if not re.match(passwd_regex, password):
                return JsonResponse({"message": "PASSWORD_ERROR"}, status=400)

            User.objects.create(
                name     = name,
                email    = email,
                passwd   = password,
                phone    = phone
                )
            return JsonResponse({"message": "Success"}, status = 201)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class LogInView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data["email"]
            password = data["password"]

            if email == "" or password == "":
                return JsonResponse({"result" : "KEY_ERROR"}, status=400)

            if not User.objects.filter(email=email).exists():
                raise User.DoesNotExist

            user_info = User.objects.get(email=email)

            if user_info.passwd != data["password"]:
                raise User.DoesNotExist

            return JsonResponse({"result" : "SUCCESS"}, status=200)

        except User.DoesNotExist:
              return JsonResponse({"result" : "INVALID_USER"}, status=500)





