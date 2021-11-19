import json
import re

from django.http      import JsonResponse
from django.views     import View

from users.models     import User
from django.db        import IntegrityError

class log_in(View):
    def Post(self, request):
        try:
            data = json.loads(request.body)
    
            user_list     = User.objects.all()
            password_list = User.objects.all()

            email    = data["email"]
            password = data["password"]

            if email not in user_list:
                return JsonResponse({"MESSAGE":"INVALID_USER"}, status = 401) 
            elif password not in password_list: 
                return JsonResponse({"MESSAGE":"INVALID_USER"}, status = 401)

        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status = 400)
        
        return JsonResponse({"MESSAGE" : "SUCCESS"}, status = 201)

        

class UsersView(View):
    def post(self, request):
      
        try:
            data       = json.loads(request.body)
            email      = data["email"]
            password   = data["password"]

            email_validation    = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            password_validation = re.compile('(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%*^&+=])([a-zA-Z0-9!@#$%*^&+=]{8,})')
            
            if not email_validation.match(email):
                return JsonResponse({},) #함수니까, return이 되면, 함수가 종료
            
            if not password_validation.match(password):
                raise KeyError
                
            User.objects.create(
                name     = data["name"],
                email    = data["email"],
                password = data["password"],
                contact  = data["contact"],
            )

            return JsonResponse({"MESSAGE" : "SUCCESS"}, status = 201)
        
        except IntegrityError:
            return JsonResponse({"user_MESSAGE":"user_ERROR"}, status = 400)

        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status = 400)
       
        
       

