import json

from django.http.response   import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from .models                import User
from .validation            import Log_in,Signup_password, Signup_email

class SignUpView(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            name         = data["name"]
            email        = data['email']
            password     = data["password"]
            phone        = data["phone"]

            Signup_email(email)

            Signup_password(password)

            User.objects.create(
                name     = name,
                email    = email,
                passwd   = password,
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

            Log_in(email, password)

            return JsonResponse({"message" : "SUCCESS"}, status=200)

        except ValidationError as e:
            return JsonResponse({"message": e.message}, status=400)
        except User.DoesNotExist:
              return JsonResponse({"message" : "KEY_ERROR"}, status=401)
        except KeyError:
              return JsonResponse({"message" : "KEY_ERROR"}, status=400)