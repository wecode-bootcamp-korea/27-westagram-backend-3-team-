import json, bcrypt, jwt

from django.http.response   import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from .models                import User
from .validation            import signup_password, signup_email
from my_settings            import SECRET_KEY, ALGORITHM

class SignUpView(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            name         = data["name"]
            email        = data['email']
            password     = data["password"]
            phone        = data["phone"]

            signup_email(email)

            signup_password(password)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message" : "EMAIL_ALREADY_EXISTS"}, status=400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                name     = name,
                email    = email,
                password = hashed_password,
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
            data  = json.loads(request.body)         
            user  = User.objects.get(email=data["email"])
            if bcrypt.checkpw(data["password"].encode('utf-8'), user.password.encode('utf-8')):
                access_token = jwt.encode({'id' : user.id}, SECRET_KEY, algorithm=ALGORITHM)
                return JsonResponse({"message" : access_token}, status=200)    
                
            return JsonResponse({"message" : "UNAUTHORIZATION"}, status=401)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message" : "DOESNOTEXIST"}, status=401)