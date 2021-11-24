import json

from django.http                import JsonResponse
from django.views               import View
from posting.models             import Post

from users.models               import User
from users.token_deco           import deco_token


class PostView(View):
    @deco_token
    def post(self, request):
        data                = json.loads(request.body)
        user                = User.objects.get(email = data["email"])

        Post.objects.create(
            user_id         = user.id,
            image           = data["image"],
            describe        = data["describe"]    
        )

        return JsonResponse({'MESSAGE':'CREATED'}, status = 201)
    
    def get(self, request):
        posts               = Post.objects.all()
        results = []

        for post in posts:
            results.append(
                {
                    "name"          : Post.users.User.name,
                    "describe"      : post.describe,
                    "time"          : post.created_at,
                    "image"         : post.image
                }
            )
        return JsonResponse({'results':results}, status=200)
        

# class SignUpView(View):
#     def post(self, request):
      
#         try:
#             data     = json.loads(request.body)
#             name     = data["name"]
#             email    = data["email"]
#             password = data["password"]
#             contact  = data["contact"]
           
#             validation_email(email)
#             validation_password(password)
            
#             if User.objects.filter(email = email).exists():
#                 return JsonResponse({"MESSAGE":"User_Already_Exists"}, status = 400)

#             hashed_password = bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

#             User.objects.create(
#                 name     = name,
#                 email    = email,
#                 password = hashed_password,
#                 contact  = contact
#             )

#             return JsonResponse({"MESSAGE":"SUCCESS"}, status = 201)
        
#         except ValidationError as e:
#             return JsonResponse({"MESSAGE":e.message}, status = 400)

#         except KeyError:
#             return JsonResponse({"MESSAGE":"KEY_ERROR"}, status = 400)

