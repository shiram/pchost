from django.urls import path
from onboarding import views

urlpatterns = [
    path("", views.register, name="onboard"),
    path("/signin", views.login, name="signin")
]