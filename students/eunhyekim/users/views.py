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

            email_validation    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            password_validation = '(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%*^&+=])([a-zA-Z0-9!@#$%*^&+=]{8,})'
            
            if not re.match(email_validation, email) or not re.match(password_validation, password):
                return JsonResponse({"MESSAGE":"Validation Error"}, status = 400)
        
                
            User.objects.create(
                name     = data["name"],
                email    = data["email"],
                password = data["password"],
                contact  = data["contact"],
            )

            return JsonResponse({"MESSAGE":"SUCCESS"}, status = 201)
        
        except IntegrityError:
            return JsonResponse({"MESSAGE":"REGISTERED_USER"}, status = 400)

        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status = 400)