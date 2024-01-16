from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django import forms
from django.views.generic.base import TemplateView
from apps.products.models import (
    Products,
    Order,
    OrderDetail,
    Indicator,
    CategoryProduct,
)
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from apps.products.forms import ProductsForm, OrderForm, DetailForm
from django.urls import reverse_lazy

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# @method_decorator(login_required, name="dispatch")


# Create your views here.
@method_decorator(login_required, name="dispatch")
class ListProducts(ListView):
    model = Products
    template_name = "products/offers.html"

    def get_queryset(self) -> QuerySet[Any]:
        categorias_indicator = CategoryProduct.objects.filter(categories__isnull=False)
        queryset = Products.objects.filter(category_product__in=categorias_indicator)
        return queryset

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["products"] = self.get_queryset()
        context["indicators"] = Indicator.objects.all()
        return context


@method_decorator(login_required, name="dispatch")
class MenuListView(ListView):
    model = Products
    template_name = "products/menu.html"
    context_object_name = "products"
    queryset = Products.objects.filter(state=True)


@method_decorator(login_required, name="dispatch")
class NewsTemplateView(TemplateView):
    template_name = "products/news.html"


@method_decorator(login_required, name="dispatch")
class GalleryTemplateView(ListView):
    model = Products
    context_object_name = "products"
    template_name = "products/gallery.html"


@method_decorator(login_required, name="dispatch")
class ProductDetailView(DetailView):
    template_name = "products/product_info.html"
    model = Products


@method_decorator(login_required, name="dispatch")
class CreateProduct(CreateView):
    template_name = "products/create_product.html"
    form_class = ProductsForm

    def get_success_url(self) -> str:
        return reverse_lazy("product_info", kwargs={"pk": self.object.pk})


@method_decorator(login_required, name="dispatch")
class DeleteProduct(DeleteView):
    model = Products
    template_name = "products/products_confirm_delete.html"

    def get_success_url(self) -> str:
        return reverse_lazy("menu") + "?ok"


@method_decorator(login_required, name="dispatch")
class UpdateProduct(UpdateView):
    model = Products
    form_class = ProductsForm
    template_name = "products/update_product.html"

    def get_success_url(self) -> str:
        return reverse_lazy("product_info", args=[self.object.id]) + "?updated"


@method_decorator(login_required, name="dispatch")
class OrderView(DetailView):
    model = Order
    template_name = "products/order.html"


@method_decorator(login_required, name="dispatch")
class OrderCreate(CreateView):
    form_class = OrderForm
    template_name = "products/order_create.html"

    def get_success_url(self) -> str:
        return reverse_lazy("order")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["user"].widget = forms.HiddenInput()
        form.fields["order_detail"].widget = forms.CheckboxSelectMultiple()
        form.fields["total"].widget = forms.HiddenInput()

        return form


@method_decorator(login_required, name="dispatch")
class DetailCreate(CreateView):
    form_class = DetailForm
    template_name = "products/detail_create.html"
    success_url = reverse_lazy("order_create")


"""def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["username"].widget = forms.TextInput(
            attrs={"class": "form-control mb-2"}
        )
        form.fields["email"].widget = forms.EmailInput(
            attrs={"class": "form-control mb-2"}
        )
        form.fields["password1"].widget = forms.PasswordInput(
            attrs={"class": "form-control mb-2"}
        )
        form.fields["password2"].widget = forms.PasswordInput(
            attrs={"class": "form-control mb-2"}
        )
        return form"""
