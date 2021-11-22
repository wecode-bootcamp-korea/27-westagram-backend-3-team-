import json

from django.http                import JsonResponse
from django.views               import View
from django.core.exceptions     import ValidationError

from users.models               import User
from users.validation           import Validation_Email, Validation_Password


class SignInView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            password = User.objects.get(email = data["email"]).password
            
            if data['password'] != password:
                return JsonResponse({'message':'INVALID_USER'}, status = 400)
            return JsonResponse({'message':'SUCCESS'},status = 200)
        
        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status = 401)

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
           
            Validation_Email(email)
            Validation_Password(password)
            
            User.objects.create(
                name     = name,
                email    = email,
                password = password,
                contact  = contact
            )

            return JsonResponse({"MESSAGE":"SUCCESS"}, status = 201)
        
        except ValidationError as e:
            return JsonResponse({"MESSAGE":e.message}, status = 400)

        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status = 400)