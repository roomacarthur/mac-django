
from django.urls import path
from .views import Forum

urlpatterns = [
    path('', Forum.as_view(), name="forum"),
]
