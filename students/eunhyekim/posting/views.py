import json

from django.http                import JsonResponse
from django.views               import View
from django.core.exceptions     import ValidationError

from posting.models             import Post
from utils.decorator_sign_in    import sign_in_decorator
from utils.validator            import validation_url


class PostView(View):
    @sign_in_decorator
    def post(self, request):              
           
        try:
            user     = request.user
            data     = json.loads(request.body)
            describe = data["describe"]
            image    = data["image"]

            validation_url(image)

            Post.objects.create(
                user_id         = user.id,
                image           = image,
                describe        = describe    
            )

            return JsonResponse({'MESSAGE':'CREATED'}, status = 201)

        except ValidationError as e:
            return JsonResponse({"MESSAGE":e.message}, status = 400)
        
        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status = 400)

    @sign_in_decorator                               #get에서는 데코레이터가 필요 없나?, 권한에 따라서 내가 올린 게시물 보려면 로그인해야 함, 일반 유저는 로그인 과정 거치지 않아도 확인 할 수 있게 분리 할 수 있음                                           
    def get(self, request):
        posts   = Post.objects.all()
        results = []

        for post in posts:
            results.append(
                {
                    "user_name"  : post.user.name,
                    "description": post.describe,
                    "posted_at"  : post.created_at,
                    "image"      : post.image
                }
            )
        return JsonResponse({'results':results}, status=200)
        

