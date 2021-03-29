from django.urls import path

from .views import ListCreateView, AddProfileView, DeleteUserView

urlpatterns = [
    path('', ListCreateView.as_view()),
    path('/<int:pk>/profile', AddProfileView.as_view()),
    path('<int:pk>', DeleteUserView.as_view())
]
