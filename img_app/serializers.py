from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Picture
class PictureSerializer(ModelSerializer):
    class Meta:
        model = Picture
        exclude = ('creator',)

class UserSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'email')
        model = User
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.save()

        return user


