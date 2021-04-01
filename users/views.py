from django.contrib.auth import get_user_model
from rest_framework import request, status
from rest_framework.generics import CreateAPIView, get_object_or_404, \
    DestroyAPIView, ListAPIView, GenericAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from user_profile.serializers import ProfileSerializer
from users.serializers import UserSerializers

UserModel = get_user_model()


class AllUsersListView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAdminUser]


class UserListView(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializers

    def get_object(self):
        print(self.request.user)
        # user = get_object_or_404(UserModel, pk=user_id)
        # user.save()
        return self.request.user

    # def get(self, request, *args, **kwargs):
    #     pk = self.request.user.id
    #     print(pk)
    #     user = get_object_or_404(UserModel, pk=pk)
    #     serializator = UserSerializers(data=user)
    #     return Response(user)


class CreateView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializers
    permission_classes = [AllowAny]


class UserToAdmin(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAdminUser]

    def patch(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        user.is_staff = True
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
