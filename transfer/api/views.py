from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin , CreateModelMixin , RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from account.models import User
from .serializers import BankAccountSerilizer , VirtualAccountSerializer
from transfer.models import BankAccount
from helpers.geniopay.wallet import createWallet


class BankAccountView(
    CreateModelMixin,
    RetrieveModelMixin,
    GenericViewSet
    ):
    permission_classes = [IsAuthenticated,]
    queryset = BankAccount.objects.all()
    serializer_class = VirtualAccountSerializer
    lookup_field = "id"
    lookup_value_regex = "[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}"

    def get_object(self, queryset=None):
        return BankAccount.objects.filter(id=self.kwargs["id"]).first()
    
    @swagger_auto_schema(
        tags=['Virtual Account'], 
        operation_summary="Create Virtual Account",
        operation_description="This creates the user virtual account",
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        auth_token = self.request.user.geniopay_key
        user_id = self.request.user.geniopay_user_id
        user = self.request.user.id
        headers = self.get_success_headers(serializer.data)
        response  = createWallet( auth_token = auth_token , user_id = user_id ,user = user , data_body = serializer.data)
        if response.status_code == 201:
            return Response(response.json() , status=status.HTTP_201_CREATED, headers=headers)
        
        return Response(response.json() , status=status.HTTP_400_BAD_REQUEST, headers=headers)
        
    

    @swagger_auto_schema(
        tags=['Virtual Account'], 
        operation_summary="Get Virtual Account",
        operation_description="This returns the user virtual account.",
    )
    def retrieve(self, request, *args, **kwargs):
        try:
            print(self.kwargs["id"])
            instance = BankAccount.objects.filter(id=self.kwargs["id"]).first()
        except Exception as e:
            return Response({"message": str(e)})
        else:
            serializer = BankAccountSerilizer(instance)
            return Response(serializer.data)
        