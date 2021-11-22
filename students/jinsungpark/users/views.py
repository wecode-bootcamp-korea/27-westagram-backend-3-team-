from django.db            import IntegrityError

from django.http.response import JsonResponse

import re
import json

from django.views         import View
from .models              import User


# Create your views here.
class SignUpView(View):
    def post(self, request):
        try:
            data             = json.loads(request.body)
            email_regex = '^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$'
            passwd_regex = '^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$'

            if re.match(email_regex, data["email"]) is None:
                return JsonResponse({"message": "EMAIL_ERROR"}, status=400)

            if re.match(passwd_regex, data["password"]) is None:
                return JsonResponse({"message": "PW_ERROR"}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message" : "INVALID_USER"}, status=401) 

            User.objects.create(
                name     = data["name"],
                email    = data["email"],
                passwd   = data["password"],
                phone    = data["phone"],
                )
            return JsonResponse({"message": "Success"}, status = 201)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        except IntegrityError:
            return JsonResponse({"message": "EMAIL_ERROR"}, status=400)


