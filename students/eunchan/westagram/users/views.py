import json, re

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from users.models           import Member

email_regexp    = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
password_regexp = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&(){}\[\]])[A-Za-z\d@$!%*#?&(){}\[\]]{8,}$"

class SignupView(View):
    def post(self, request):

        try:
            data         = json.loads(request.body) 
            name         = data["name"]
            email        = data["email"]
            password     = data["password"]
            phone_number = data["phone_number"]
            information  = data.get("information","")

            if not re.match(email_regexp, email): 
                return JsonResponse({'massage':"EMAIL_ERROR"}, status=400)

            if not re.match(password_regexp , password):
                return JsonResponse({'massage':"PASSWORD_ERROR"}, status=400)

            member = Member(
                name         = name,
                email        = email,
                password     = password,
                phone_number = phone_number,
                information  = information
            )
            member.full_clean() 
            member.save()

            return JsonResponse({'massage':"SUCCESS"}, status=201)

        except ValidationError :
            return JsonResponse({'massage':"VALIDATION_ERROR"}, status=400)

        except KeyError :
            return JsonResponse({'massage':"KEY_ERROR"}, status=400)



