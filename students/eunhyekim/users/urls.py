from django.urls        import path
from users.views        import LogInView, SignUpView

urlpatterns = [
    path('', SignUpView.as_view()),
    path('login/', LogInView.as_view())
]