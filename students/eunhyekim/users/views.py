import json, re

from django.db.models.fields    import EmailField
from django.http                import JsonResponse
from django.urls                import exceptions
from django.views               import View
from django.db                  import IntegrityError
from django.core.exceptions     import FieldDoesNotExist

from users.models               import User


class LogInView(View):
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
            email    = data["email"]
            password = data["password"]

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