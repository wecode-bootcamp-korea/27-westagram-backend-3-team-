from django.core.checks.messages import Error
from django.db.models.fields import EmailField
from django.shortcuts import render

from django.http import request
from django.http.response import JsonResponse

import re
import json

from django.views import View
from .models import User


# Create your views here.
class SignUpView(View):
    def post(self, request):
        try:
            data             = json.loads(request.body)
            email_condition  = '^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$'
            passwd_condition = '^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$'

            if re.match(email_condition, data["email"]) is None:
                return JsonResponse({"message": "EMAIL_ERROR"}, status=400)
            elif re.match(passwd_condition, data["passwd"]) is None:
                return JsonResponse({"message": "PW_ERROR"}, status=400)
        except Exception:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        else:
            User.objects.create(
            name     = data["name"],
            email    = data["email"],
            password = data["passwd"],
            phone    = data["phone"],
            )
            return JsonResponse({"message": "Success"}, status = 201)
