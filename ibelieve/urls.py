from django.contrib import admin
from django.urls import include, path
from ibelieve.views import landingPage, homePage, contactPage, worksPage, portfolioPage

urlpatterns = [
    path("landing/", landingPage, name="landingpage"),
    path("", homePage, name="homepage"),
    path("works/", worksPage, name="workspage"),
    path("contact/", contactPage, name="contactpage"),
    path("portfolio/", portfolioPage, name="portfoliopage"),
]