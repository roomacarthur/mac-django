
from django.urls import path
from .views import Social

urlpatterns = [
    path('', Social.as_view(), name="social"),
]
