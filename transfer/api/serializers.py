from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from  transfer.models import BankAccount , Balance , AccountType , BankAddress , FundingAccounts , AccountDetails


class BalanceSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        exclude = ('id', 'created_date', 'modified_date',)

    def create(self, validated_data):
        return super().create(validated_data)


class AccountTypeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = AccountType
        exclude = ('id', 'created_date', 'modified_date','deleted')

    def create(self, validated_data):
        return super().create(validated_data)


class BankAddressSerilizer(serializers.ModelSerializer):
    class Meta:
        model = BankAddress
        exclude = ('id', 'created_date', 'modified_date','deleted',)

    def create(self, validated_data):
        return super().create(validated_data)


class FundingAccountsSerilizer(serializers.ModelSerializer):
    bank_address = BankAddressSerilizer()
    class Meta:
        model = FundingAccounts
        fields = ('bank_name', 'bank_address', 'payment_type', 'identifier_type', 'identifier_value', 'account_number_type', 'account_number', 'funding_instructions')

    def create(self, validated_data):
        return super().create(validated_data)


class AccountDetailsSerilizer(serializers.ModelSerializer):
    funding_accounts = FundingAccountsSerilizer( many = True )
    class Meta:
        model = AccountDetails
        fields = ('currency', 'country', 'payment_reference', 'funding_accounts')

    def create(self, validated_data):
        funding_accounts_data = validated_data.pop('funding_accounts', None)
        account_details = super().create(validated_data)
        if funding_accounts_data:
            for funding_account_data in funding_accounts_data:
                bank_address_data = funding_account_data.pop('bank_address', None)
                if bank_address_data:
                    bank_address_instance = BankAddress.objects.create(**bank_address_data)
                    funding_account_instance = FundingAccounts.objects.create(
                        bank_address=bank_address_instance,
                        **funding_account_data
                    )

                    account_details.funding_accounts.add(funding_account_instance)

        return account_details



class BankAccountSerilizer(WritableNestedModelSerializer):
    available_balance = BalanceSerilizer()
    ledger_balance = BalanceSerilizer()
    pending_balance = BalanceSerilizer()
    blocked_balance = BalanceSerilizer()
    total_incoming = BalanceSerilizer()
    account_details = AccountDetailsSerilizer()
    account_type = AccountTypeSerilizer()
    class Meta:
        model = BankAccount
        exclude = ('created_date', 'modified_date','account_user')

    def create(self, validated_data):
        return super().create(validated_data)



class VirtualAccountSerializer(serializers.Serializer):
    friendly_name = serializers.CharField(max_length=20)
    currency = serializers.CharField()
    default = serializers.BooleanField()

    


class TransactionalPinSerlizer(serializers.Serializer):
    pin = serializers.IntegerField()

