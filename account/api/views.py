from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin , CreateModelMixin 
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny , IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from account.models import User
from .serializers import SignupSerializer , EmailVerifySerilaizer, UserInfoSerilizer
from helpers.geniopay.register import verifyEmail, genioRegister
from account.tasks import obtainAuthToken , obtainGenioPyaUserID




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
        


