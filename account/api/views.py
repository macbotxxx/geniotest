from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin , CreateModelMixin 
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from account.models import User
from .serializers import SignupSerializer , EmailVerifySerilaizer
from helpers.geniopay.register import verifyEmail, genioRegister
from account.tasks import obtainAuthToken , obtainGenioPyaUserID




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
        res = obtainGenioPyaUserID.delay(token = "30bc361193db5caadcfbb737a79a0dd35e73bb2d", email ="xaporaj208@pursip.com")
        # res = verifyEmail( body_data = serializer.data )
        # if res['status_code'] == 201:
        #     # updating the user account on geniopay email verification
        #     accountVerify = User.objects.filter(email = serializer.data.get("email")).first()
        #     accountVerify.email_verification = True
        #     accountVerify.save()
        #     return Response(res , status=status.HTTP_201_CREATED)
        print(res)
        
        return Response( status=status.HTTP_400_BAD_REQUEST)
        


