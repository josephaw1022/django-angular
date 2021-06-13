from django.urls import path
from frontend.views import *

urlpatterns = [
    path('', Index.as_view(), name='index')
]
