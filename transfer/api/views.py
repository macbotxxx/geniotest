from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin , CreateModelMixin 
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from account.models import User
from .serializers import TransactionalPinSerlizer


class TransferPin(
    CreateModelMixin,
    GenericViewSet
    ):
    pass