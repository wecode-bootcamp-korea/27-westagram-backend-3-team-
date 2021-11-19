from django.urls import path
from .views import *

urlpatterns = [
    path("",UsersView.as_view())
]
