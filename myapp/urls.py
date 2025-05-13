# forms_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_eform, name="user-eform"),
    path("success/", views.success, name="eform-success"),
]
