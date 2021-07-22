from django.urls import path

from apps.users.views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
