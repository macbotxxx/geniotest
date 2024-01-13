from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from account.models import User as UserType



User = get_user_model()


class UserSerializer(serializers.ModelSerializer[UserType]):
    class Meta:
        model = User
        ref_name = "defaultusername"
        fields = ["name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
        }


class EmailVerifySerilaizer(serializers.Serializer):
    email = serializers.EmailField()
    key = serializers.CharField()


class SignupSerializer(serializers.ModelSerializer[UserType]):
    
    ACCOUNT_TYPE = (
        ('PERSONAL', _('PERSONAL')),
        ('BUSINESS', _('BUSINESS')),
    )

    password = serializers.CharField(write_only=True)

    email = serializers.EmailField(
        help_text=_("The primary email address of the user. An Email verification will be required upon successful registration."))
    
    account_type = serializers.ChoiceField(
        choices=ACCOUNT_TYPE,
        help_text=_("The primary email address of the user. An Email verification will be required upon successful registration."))
    
       
    class Meta:
        model = User
        ref_name = "wey_registration"
        fields = [ 'first_name', 'last_name','email', 'password','account_type','country','time_zone','language','mobile','accept_terms','agreed_to_data_usage']
   
    def get_cleaned_data(self):
            return {
                'first_name': self.validated_data.get('first_name'),
                'last_name': self.validated_data.get('last_name'),
                'email': self.validated_data.get('email'), 
                'account_type': self.validated_data.get('account_type'),
                'country': self.validated_data.get('country'),
                'time_zone': self.validated_data.get('time_zone'),
                'language': self.validated_data.get('language'),
                'mobile': self.validated_data.get('mobile'),
                'accept_terms': self.validated_data.get('accept_terms'),
                'agreed_to_data_usage': self.validated_data.get('agreed_to_data_usage'),
                'password': self.validated_data.get('password'),          
            }
            

    # def validate_email(self, value):
    #     user_exist= User.objects.filter(email=value).exists()
    #     if user_exist:
    #         raise serializers.ValidationError("This email address used is already taken. Please login!")
    #     return value

    def validate_email_verification(self,value):
        if not value:
            raise serializers.ValidationError("email verification is required")
        return value


    def validate_first_name(self,value):
        if not value:
            raise serializers.ValidationError("first name field is required")
        return value

    def validate_last_name(self,value):
        if not value:
            raise serializers.ValidationError("last name field is required")
        return value
    
    def validate_mobile(self,value):
        if not value:
            raise serializers.ValidationError("mobile number is required and cant be empty")
        return value
    
    def validate_account_type(self,value):
        if not value:
            raise serializers.ValidationError("you have to select from the given account types")
        return value
    
    def validate_country(self,value):
        if not value:
            raise serializers.ValidationError("Country cant be empty")
        return value
    
    def validate_time_zone(self,value):
        if not value:
            raise serializers.ValidationError("timezone is required")
        return value
    

    def save(self, **kwargs):
        cleaned_data = self.get_cleaned_data()
        # creating Geniopay account
        # res = genioRegister(body_data = cleaned_data)
        # if res[0] == 201:
        #     user = User(**cleaned_data)
        #     user.set_password(cleaned_data["password"])
        #     user.save()
        #     return user
        # raise serializers.ValidationError(res[1])
        user = User(**cleaned_data)
        user.set_password(cleaned_data["password"])
        user.save()
        return user
        
    


class TestEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    message = serializers.CharField()
   
    