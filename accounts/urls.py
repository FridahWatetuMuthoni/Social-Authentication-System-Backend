from django.urls import path, include, re_path
from .views import TwitterLogin,GoogleLogin, GenderChoices
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
from dj_rest_auth.views import LoginView, LogoutView,PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('twitter/', TwitterLogin.as_view(), name='twitter_login'),
    path('google/', GoogleLogin.as_view(), name='google_login'),
    path('genders/', GenderChoices.as_view(), name='gender_choices'),
    path('register/', RegisterView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify-email/',VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/',VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',VerifyEmailView.as_view(), name='account_confirm_email'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]