from django.contrib import admin
from django.urls import include, path
from theme.views import landingPage, examplePage

urlpatterns = [
    path("landingpage/", landingPage, name="landingpage"),
    path("", examplePage, name="example"),
]