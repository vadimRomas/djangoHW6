from django.urls import path

from .views import CreateView,\
 AddProfileView, DeleteUserView, UserToAdmin, UserListView, AllUsersListView

urlpatterns = [
    path('/register', CreateView.as_view()),
    path('/<int:pk>/profile', AddProfileView.as_view()),
    path('/<int:pk>', DeleteUserView.as_view()),
    path('/<int:pk>/toadmin', UserToAdmin.as_view()),
    path('', UserListView.as_view()),
    path('allusers', AllUsersListView.as_view())
]
