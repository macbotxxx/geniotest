from rest_framework import serializers

class TransactionalPinSerlizer(serializers.Serializer):
    pin = serializers.IntegerField()

