import re, json, bcrypt

from django.http.response   import JsonResponse
from django.views           import View

from .models                import User

class SignUpView(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            email        = data['email']
            passwd       = data["password"]
            email_regex  = '^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$'
            passwd_regex = '^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$'

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message" : "USER_ALREADY_EXISTS"}, status=400)

            if not re.match(email_regex, email):
                return JsonResponse({"message": "EMAIL_ERROR"}, status=400)

            if not re.match(passwd_regex, passwd):
                return JsonResponse({"message": "PASSWORD_ERROR"}, status=400)

            User.objects.create(
                name     = data["name"],
                email    = email,
                passwd   = passwd,
                phone    = data["phone"],
                )
            return JsonResponse({"message": "Success"}, status = 201)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)



