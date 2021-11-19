import json
import re

from django.http      import JsonResponse
from django.views     import View

from users.models     import User

class UsersView(View):
    def post(self, request):
        data       = json.loads(request.body)
        email_list = User.objects.all()
        email      = data["email"]
        password   = data["password"]

        
        try:
            email_validation    = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            if not email_validation.match(email):
                raise Exception   #({"MESSAGE":"KEY_ERROR"})
        except Exception:
            return JsonResponse({"email_MESSAGE":"KEY_ERROR"}, status = 400)
            
        try:
            password_validation = re.compile('(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%*^&+=])([a-zA-Z0-9!@#$%*^&+=]{8,})')
            if not password_validation.match(password):
                raise Exception   #({"MESSAGE":"KEY_ERROR"})
        except Exception:
            return JsonResponse({"password_MESSAGE":"KEY_ERROR"}, status = 400)
        
        else:
            User.objects.create(
                name     = data["name"],
                email    = data["email"],
                password = data["password"],
                contact  = data["contact"],
            )
    

        return JsonResponse({"MESSAGE" : "SUCCESS"}, status = 201)
     