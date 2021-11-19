import json
import re

from django.http      import JsonResponse
from django.views     import View

from users.models     import User
from django.db        import IntegrityError

        
class SignUpView(View):
    def post(self, request):
      
        try:
            data       = json.loads(request.body)
            email      = data["email"]
            password   = data["password"]

            email_validation    = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            password_validation = re.compile('(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%*^&+=])([a-zA-Z0-9!@#$%*^&+=]{8,})')
            
            if not email_validation.match(email):
                return JsonResponse({"MESSAGE":"email_ERROR"}, status = 400) 
            
            if not password_validation.match(password):
                return JsonResponse({"MESSAGE":"password_ERROR"}, status = 400)
                
            User.objects.create(
                name     = data["name"],
                email    = data["email"],
                password = data["password"],
                contact  = data["contact"],
            )

            return JsonResponse({"MESSAGE":"SUCCESS"}, status = 201)
        
        except IntegrityError:
            return JsonResponse({"user_MESSAGE":"user_ERROR"}, status = 400)

        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status = 400)