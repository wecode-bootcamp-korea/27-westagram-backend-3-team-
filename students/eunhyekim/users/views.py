import json, bcrypt, jwt

from django.http                import JsonResponse
from django.views               import View
from django.core.exceptions     import ValidationError

from users.models               import User
from users.validation           import validation_email, validation_password
from my_settings                import SECRET_KEY, ALGORITHM


class SignInView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            user     = User.objects.get(email = data["email"])
        
            if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                access_token = jwt.encode({'id':user.id}, SECRET_KEY, algorithm = ALGORITHM)
          
                return JsonResponse({'TOKEN': access_token}, status = 200)

            return JsonResponse({'MESSAGE':"UNAUTHORIZED"}, status = 401) 

        except User.DoesNotExist:
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status = 401)

        except KeyError:
            return JsonResponse({'MESSAGE' :'KEY_ERROR'}, status = 400)


class SignUpView(View):
    def post(self, request):
      
        try:
            data     = json.loads(request.body)
            name     = data["name"]
            email    = data["email"]
            password = data["password"]
            contact  = data["contact"]
           
            validation_email(email)
            validation_password(password)
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({"MESSAGE":"User_Already_Exists"}, status = 400)

            hashed_password = bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                name     = name,
                email    = email,
                password = hashed_password,
                contact  = contact
            )

            return JsonResponse({"MESSAGE":"SUCCESS"}, status = 201)
        
        except ValidationError as e:
            return JsonResponse({"MESSAGE":e.message}, status = 400)

        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status = 400)