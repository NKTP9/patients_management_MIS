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
    path('hospital_info/<int:medical_facility_id>', views.get_hospital, name="get_hospital"),
    path('appointment/<int:paramedic_id>', views.appointment, name="appointment"),
]
