# Django Project

## Third Party Installation

```sh

## for apis
pip install django
pip install djangorestframework

## for authentication system
pip install django-allauth
pip install dj-rest-auth

## for CORS
pip install django-cors-headers

## for documentation
pip install drf-specatcular

## creating the schema

python manage.py spectacular --file schema.yml
```

## DJ-REST-AUTH

### Features

1. User Registration with activation
2. Login/Logout
3. Retrieve/Update the Django User model
4. Password change
5. Password reset via e-mail
6. Social Media authentication

### Apps structure

1. dj_rest_auth has basic auth functionality like login, logout, password reset and password change.
2. dj_rest_auth.registration has logic related with registration and social media authentication

## Dj-rest-auth settings

```python

#settings.py

INSTALLED_APPS = (
    'rest_framework',
    'rest_framework.authtoken', #activate token authentication
    'dj_rest_auth'
)
```

```python
#urls.py
from django.urls import path, include

urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls'))
]

```

## Registration (optional)

1. If you want to enable standard registration process you will need to install django-allauth by using pip install 'dj-rest-auth[with_social]'.
2. Add django.contrib.sites, allauth, allauth.account, allauth.socialaccount and dj_rest_auth.registration apps to INSTALLED_APPS in your django settings.py:
3. Add SITE_ID = 1 to your django settings.py

```python

#setting.py

INSTALLED_APPS = (
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken', #activate token authentication
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
)

SITE_ID = 1
```

```python
#urls.py
from django.urls import path, include

urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]

```

```python
#views.py

from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.social_serializers import TwitterLoginSerializer
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client


class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter

"""
The GOOGLE_REDIRECT_URL value is the URL that you want Google to redirect the user to after a successful login.
"""
CALLBACK_URL_YOU_SET_ON_GOOGLE=''
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = CALLBACK_URL_YOU_SET_ON_GOOGLE
    client_class = OAuth2Client
```
