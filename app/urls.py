from django.urls import path
from . import views
from .api import *

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name="hello"),
    path('api/register/', RegisterApi.as_view(), name="register"),
]
