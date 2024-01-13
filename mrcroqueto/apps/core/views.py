from apps.users.models import User
from django.views.generic.base import TemplateView
from apps.products.models import Products
from django.views.generic.list import ListView


# Create your views here.
class HomePageView(TemplateView):
    template_name = "core/home.html"


class AboutTemplateView(TemplateView):
    template_name = "core/about.html"


class ContactTemplateView(TemplateView):
    template_name = "core/contact.html"
