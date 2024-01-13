from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin , CreateModelMixin , RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from account.models import User
from .serializers import BankAccountSerilizer
from transfer.models import BankAccount


class BankAccountView(
    CreateModelMixin,
    RetrieveModelMixin,
    GenericViewSet
    ):
    permission_classes = [IsAuthenticated,]
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerilizer
    lookup_field = "id"
    lookup_value_regex = "[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}"

    def get_object(self, queryset=None):
        return BankAccount.objects.filter(id=self.kwargs["id"]).first()
    
    @swagger_auto_schema(
        tags=['Virtual Account'],  # Add your desired tag(s) here
        operation_summary="Create Virtual Account",
        operation_description="This endopint creates a new Customer profile.",
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # print(serializer.data)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        serializer.save(account_user = self.request.user )


    def retrieve(self, request, *args, **kwargs):
        
        try:
            instance = self.get_object()
        except Exception as e:
            return Response({"message": str(e)})
        else:
            # any additional logic
            serializer = self.get_serializer(instance)

            return Response(serializer.data)
        