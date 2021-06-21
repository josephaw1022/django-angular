from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username',  "email",
                  "password", 'first_name', 'last_name']

        def create(self, validated_data):

            user = User.objects.create(
                validated_data['username'],
                None,
                make_password(validated_data['password'])
            )

            return user
