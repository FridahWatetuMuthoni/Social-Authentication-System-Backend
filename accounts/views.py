from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.social_serializers import TwitterLoginSerializer
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
class GenderChoices(APIView):
    def get(self, request):
        choices = CustomUser.GENDER_CHOICES
        return Response(choices)


# class UserRedirectView(LoginRequiredMixin, RedirectView):
#     """
#     This view is needed by the dj-rest-auth-library in order to work the google login. It's a bug.
#     """

#     permanent = False

#     def get_redirect_url(self):
#         return 'http://127.0.0.1:5173'


class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://127.0.0.1:5173'
    client_class = OAuth2Client
