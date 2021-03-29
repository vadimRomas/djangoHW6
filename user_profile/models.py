from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

def to_upload(instance, filename):
    return f'{instance.user.email}/avatars/{filename}'
# Create your models here.
class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    username = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    avatar = models.ImageField(upload_to=to_upload)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')

