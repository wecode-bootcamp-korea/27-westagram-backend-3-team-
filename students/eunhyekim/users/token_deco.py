
import json, bcrypt, jwt

from django.http                import JsonResponse

from users.models               import User
from users.views                import *
from my_settings                import SECRET_KEY, ALGORITHM

def deco_token(func):
    def access_tk(self, request, *args, **kwargs):
        try:
            data     = json.loads(request.body)
            user     = User.objects.get(email = data["email"])
        
            if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                access_token = jwt.encode({'id':user.id}, SECRET_KEY, algorithm = ALGORITHM)
          
                #return JsonResponse({'TOKEN': access_token}, status = 200)
                return func(self, request)

            return JsonResponse({'MESSAGE':"UNAUTHORIZED"}, status = 401) 

        except User.DoesNotExist:
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status = 401)

        except KeyError:
            return JsonResponse({'MESSAGE' :'KEY_ERROR'}, status = 400)
        
    
    return access_tk

# def validation_e(func):
#     def val_decorator(self, request):
#         data = json.loads(request.body)
#         email = data["email"]
#         email_validation    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
#         if not re.match(email_validation, email):
#             return JsonResponse({"message" :"Email_Invalidation"})
#         return func(self, request)
#     return val_decorator                                                        