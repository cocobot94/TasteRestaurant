from django.urls import path, include
from apps.core.views import (
    HomePageView,
    AboutTemplateView,
    ContactTemplateView,
)


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutTemplateView.as_view(), name="about"),
    path("contact/", ContactTemplateView.as_view(), name="contact"),
    path("", include("apps.products.urls")),
]
