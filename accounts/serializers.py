from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import PasswordResetSerializer
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from .forms import CustomResetPasswordForm



User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(required=False)
    date_of_birth = serializers.DateField(required=False)
    phone_number = serializers.CharField(max_length=15, required=False)
    address = serializers.CharField(required=False)
    gender = serializers.ChoiceField(choices=CustomUser.GENDER_CHOICES, required=False)

    def get_cleaned_data(self):
        cleaned_data = super().get_cleaned_data()
        cleaned_data['age'] = self.validated_data.get('age', None)
        cleaned_data['date_of_birth'] = self.validated_data.get('date_of_birth', None)
        cleaned_data['phone_number'] = self.validated_data.get('phone_number', None)
        cleaned_data['address'] = self.validated_data.get('address', None)
        cleaned_data['gender'] = self.validated_data.get('gender', None)
        cleaned_data['first_name'] = self.validated_data.get('first_name', '')
        cleaned_data['last_name'] = self.validated_data.get('last_name', '')
        return cleaned_data

    def save(self, request):
        user = super(CustomRegisterSerializer, self).save(request)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.age = self.validated_data.get('age', None)
        user.date_of_birth = self.validated_data.get('date_of_birth', None)
        user.phone_number= self.validated_data.get('phone_number', None)
        user.address = self.validated_data.get('address', None)
        user.gender = self.validated_data.get('gender', None)
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','username','email','age', 'date_of_birth', 'phone_number', 'address', 'gender' 'password1','password2',)
        
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    



class CustomPasswordResetSerializer(PasswordResetSerializer):
    @property
    def password_reset_form_class(self):
        return CustomResetPasswordForm

    def get_email_options(self):
        # Return a dictionary of email options
        email_template = "account/email/password_reset_key_message.txt"

        return {
            'domain_override': 'localhost:5173',
            "html_email_template_name": email_template,
            "from_email": "Operations Accounts <accounts@herrings.co.ke>",
        }