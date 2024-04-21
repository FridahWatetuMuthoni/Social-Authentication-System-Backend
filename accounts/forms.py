from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.adapter import get_adapter
from allauth.account.forms import ResetPasswordForm
from allauth.account.utils import user_pk_to_url_str
from django.utils import translation

""" 
At the top we import UserCreationForm and UserChangeForm which are used for creating
or updating a user. 
We also import our CustomUser model so that it can be integrated into new
CustomUserCreationForm and CustomUserChangeForm classes.
"""

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age', 'date_of_birth', 'phone_number', 'address', 'gender',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class CustomResetPasswordForm(ResetPasswordForm):
    def save(self, request, **kwargs):
        email = self.cleaned_data['email']
        token_generator = kwargs.get('token_generator')
        template = kwargs.get("email_template")
        extra = kwargs.get("extra_email_context", {})

        for user in self.users:
            uid = user_pk_to_url_str(user)
            token = token_generator.make_token(user)
            reset_url = f"http://127.0.0.1:5173/password-reset-confirm/{uid}/{token}/"
            context = {"user": user, "request": request,
                       "email": email, "reset_url": reset_url}
            context.update(extra)
            get_adapter(request).send_mail(
                "account/email/password_reset_key", email, context)
        return email