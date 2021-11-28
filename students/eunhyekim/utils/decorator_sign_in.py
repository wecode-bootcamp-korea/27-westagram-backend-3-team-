
import jwt

from django.http                import JsonResponse

from users.models               import User

from Westagram.settings         import SECRET_KEY, ALGORITHM

def sign_in_decorator(func):
    def access_token(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get("Authorization", None)   #get으로 필터링을 하면 keyerror가 나지 않고, none으로 반환, None(반환값)을 지정해줘도 됨
                                                  
            payload = jwt.decode(access_token, SECRET_KEY, algorithms = ALGORITHM)
            user  = User.objects.get(id = payload['id'])
            request.user = user
            #print(request.user)
            #print(request)
            #print(request.__dict__)
            #print(request.__dir__())
            #print(request.body)
            #print(payload) 
            #print(args)     ###
            #print(kwargs)   ###
            '''

            User object (72) #print(user)
            {'id': 72}
            <WSGIRequest: POST '/posting/posting'>   #request

            {'request' : {asdfwefsdjkfhweiufhjksldfjoiwejf...} ....  {'user' : <User: User object (72)>}}
            How?:
            request['user'] = xxx
            {'user' : xxx}

            '''

            return func(self, request, *args, **kwargs)
            
        except jwt.exceptions.DecodeError:                                                 
            return JsonResponse({'MESSAGE':'INVALID_TOKEN'}, status = 400)

        except User.DoesNotExist:
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status = 401)       
                                                                            
                                                                #세션들어라 블로그 써라 8번 가기전에 3일 후에 프로젝트 할건데 지금 하는게 낫지 않냐
                                                                #복습해라 어제 내가 분명히 복습한다고 했는데 7번하라 그래서 7번 해왔는데
                                                                #다시 복습하라고 말씀하셔서 지금부터 복습하겠습니다!
                                                                
    return access_token

# def validation_e(func):
#     def val_decorator(self, request):
#         data = json.loads(request.body)
#         email = data["email"]
#         email_validation    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
#         if not re.match(email_validation, email):
#             return JsonResponse({"message" :"Email_Invalidation"})
#         return func(self, request)
#     return val_decorator                                                        