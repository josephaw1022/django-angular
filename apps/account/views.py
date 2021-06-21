

from rest_framework.decorators import api_view
from rest_framework import response
from django.contrib.auth.models import User


@api_view(['POST'])
def CreateUserView(request):
    if request.method == 'POST':

        objects = request.data

        user = User(
            username=str(objects.get('username')),
            email=str(objects.get('email')),
            first_name=str(objects.get('first_name')),
            last_name=str(objects.get('last_name')),
        )
        user.set_password(str(objects.get('password')))
        user.save()

        return response.Response({"message": "Got some data!", "data": request.data})
    return response.Response({"message": "Hello, world!"})
