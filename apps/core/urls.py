from django.urls import path, include

from apps.core.views import (
    HomepageView,
)
from apps.core import views

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('profile/', views.profile, name="profile"),
    path('doctors/', views.doctors, name="doctors"),
    path('hospitals/', views.hospitals, name="hospitals"),

]
