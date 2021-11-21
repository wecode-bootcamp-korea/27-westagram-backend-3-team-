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
            data     = json.loads(request.body) 
            email    = data["email"]
            password = data["password"]

            if not re.match(email_regexp, email): 
                return JsonResponse({'massage':"EMAIL_ERROR"}, status=400)

            elif not re.match(password_regexp , password):
                return JsonResponse({'massage':"PASSWORD_ERROR"}, status=400)

            else : 
                member = Member(
                    name         = data["name"],
                    email        = email,
                    password     = password,
                    phone_number = data["phone_number"],
                    information  = data["information"]
                )
                member.full_clean() 
                member.save()
                return JsonResponse({'massage':"SUCCESS"}, status=201)

        except ValidationError as e:
            return JsonResponse({'massage':"VALIDATION_ERROR"+" "+str(e)}, status=400)

        except KeyError as e:
            return JsonResponse({'massage':"KEY_ERROR"+" Missing"+str(e)}, status=400)



