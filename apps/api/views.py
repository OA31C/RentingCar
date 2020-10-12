from .serializers import UserSerializer
from rest_framework import generics
from ..auth_user.models import User


class UserCreateViewAPI(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserListViewAPI(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailViewAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
