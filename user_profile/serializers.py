from rest_framework.serializers import ModelSerializer

from user_profile.models import ProfileModel


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ['id', 'username', 'age', 'avatar']
