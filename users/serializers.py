from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, ValidationError

from user_profile.serializers import ProfileSerializer

UserModel = get_user_model()


class UserSerializers(ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', 'is_staff', 'is_active', 'profile']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        try:
            user = UserModel.objects.create_user(**validated_data)
        except ValueError:
            raise ValidationError(ValueError)
        return user
