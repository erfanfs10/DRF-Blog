from rest_framework import serializers
from PIL import Image
from .models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'image', 'bio', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):

        username = self.validated_data["username"]
        email = self.validated_data["email"]
        bio = self.validated_data["bio"]
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
       
        user = User(
            username=username,
            email=email,
            bio=bio,
        )

        user.set_password(password)
        user.save()
        return user
    

class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password2 = serializers.CharField(style={"input_type": "password"}, required=True)

    def validate_current_password(self, current_password):
        if not self.context['request'].user.check_password(current_password):
            raise serializers.ValidationError({'current_password': 'Current password not match'})
        return current_password    
    
    def validate_new_password(self, new_password):
        new_password2 = self.context["request"].data["new_password2"]
        if new_password != new_password2:
            raise serializers.ValidationError({'new_password': 'new password not match'})
        return new_password
    

class ProfileSerializer(serializers.ModelSerializer ):

    class Meta:
        model = User
        fields = ("username", "email", "image", "bio")

