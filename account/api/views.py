from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin , CreateModelMixin 
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from account.models import User
from .serializers import SignupSerializer , TestEmailSerializer



class UserCreationView(
    CreateModelMixin,
    GenericViewSet
    ):
    permission_classes = [AllowAny,]
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(**kwargs)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()



