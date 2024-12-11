from django.urls import path
from .views import EventRegistrationView

urlpatterns = [
    path('event/<int:event_id>/register/', EventRegistrationView.as_view(), name='event_register'),
]