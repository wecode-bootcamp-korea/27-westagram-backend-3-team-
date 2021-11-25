import json
import re

from django.http  import JsonResponse
from django.views import View

from users.models import User

class UsersView(View):
    def post(self, request):
        try:
            data                = json.loads(request.body)
            email_regex         = re.compile("[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+")
            email_validation    = email_regex.search(data['email'])
            password_regex      = re.compile("^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$")
            password_validation = password_regex.search(data['password'])

            if not email_validation:
                return JsonResponse({'message':'이메일 형식이 올바르지 않습니다.'}, status=400)
            elif User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message':'입력하신 이메일이 이미 존재합니다.'}, status=400)
            elif not password_validation:
                return JsonResponse({'message':'문자, 숫자, 특수문자를 모두 포함한 8자리 이상만 가능합니다.'}, status=400)
            user                = User.objects.create(
                        name         = data['name'],
                        email        = data['email'],
                        password     = data['password'],
                        phone_number = data['phone_number']
            )
            return JsonResponse({'message':'SUCCESS'}, status=201)
            
        except:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

