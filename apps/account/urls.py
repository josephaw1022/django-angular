

from django.urls import path
from .views import *


urlpatterns = [
    path('createuser/', CreateUserView, name="create user")
]
