from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin , CreateModelMixin , DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny , IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from account.models import User
from .serializers import (
    SignupSerializer , EmailVerifySerilaizer, 
    UserInfoSerilizer , PinSerializer
    )
from helpers.geniopay.register import verifyEmail, genioRegister
from account.tasks import obtainAuthToken , obtainGenioPyaUserID
from helpers.common.hashkeys import wallet_encrypted_key




class UserCreationView(
    CreateModelMixin,
    GenericViewSet
    ):
    permission_classes = [AllowAny,]
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    
    @swagger_auto_schema(
        tags=['User Profile'],  # Add your desired tag(s) here
        operation_summary="Create User Profile",
        operation_description="This endopint creates a new Customer profile.",
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = request.data.get('password')
        res = genioRegister( body_data= serializer.data , password = password )
        if res.status_code == 201:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            # obtain geniopay auth token
            obtainAuthToken.delay( email = serializer.data.get('email'), password = password )
            return Response(res.json(), status=status.HTTP_201_CREATED, headers=headers)
        
        return Response( res.json() , status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()


class UserInfoView(
    ListModelMixin,
    GenericViewSet
    ):
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UserInfoSerilizer
    
    @swagger_auto_schema(
        tags=['User Profile'],  # Add your desired tag(s) here
        operation_summary="Get User Info",
        operation_description="This endpoint returns the details of an authenticated user",
    )
    def list(self, request, *args, **kwargs):
        queryset = User.objects.filter( id = self.request.user.id ).first()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)



class EmailVerificationView(
    CreateModelMixin,
    GenericViewSet
    ):
    permission_classes = [AllowAny,]
    queryset = User.objects.all()
    serializer_class = EmailVerifySerilaizer
    

    @swagger_auto_schema(
        tags=['User Profile'],  # Add your desired tag(s) here
        operation_summary="User Email Verification",
        operation_description="This endpoint verifies the user email account which the linked will be send from geniopay system",
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        res = verifyEmail( body_data = serializer.data )
        if res['status_code'] == 201:
            # updating the user account on geniopay email verification
            accountVerify = User.objects.filter(email = serializer.data.get("email")).first()
            accountVerify.email_verification = True
            accountVerify.save()
            return Response(res , status=status.HTTP_201_CREATED)
        
        return Response( res ,status=status.HTTP_400_BAD_REQUEST)
    


class PinView(
    CreateModelMixin,
    GenericViewSet
    ):
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = PinSerializer
    

    @swagger_auto_schema(
        tags=['Wallet Transfer'],  # Add your desired tag(s) here
        operation_summary="User Wallet Pin",
        operation_description="This create wallet pin",
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pin = serializer.data.get("pin")
        if not self.request.user.wallet_pin:
            wallet_pin = wallet_encrypted_key( pin = pin ) #Encrypt pin
            user_account = User.objects.filter( id = self.request.user.id ).first()
            user_account.wallet_pin = wallet_pin
            user_account.save()
            return Response( {"details":"wallet pin created successfully"} ,status=status.HTTP_201_CREATED)
        
        return Response( {"details":"wallet pin already created"} ,status=status.HTTP_400_BAD_REQUEST)
        


