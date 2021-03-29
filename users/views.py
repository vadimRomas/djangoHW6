from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView, CreateAPIView, get_object_or_404, \
    DestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser

from user_profile.serializers import ProfileSerializer
from users.serializers import UserSerializers

UserModel = get_user_model()


class ListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAdminUser]


class AddProfileView(CreateAPIView):
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        serializer.save(user=user)


class DeleteUserView(DestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAdminUser]

    # def delete(self, request, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     user = get_object_or_404(UserModel, pk=pk)
    #     serializer = UserSerializers
    #     serializer.save(user=user)
