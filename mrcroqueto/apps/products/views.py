from django.views.generic.base import TemplateView
from apps.products.models import Products
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from apps.products.forms import ProductsForm
from django.urls import reverse_lazy


# Create your views here.
class ListProducts(ListView):
    model = Products
    template_name = "products/offers.html"
    context_object_name = "products"
    queryset = Products.objects.filter(state=True)


class MenuListView(ListView):
    model = Products
    template_name = "products/menu.html"
    context_object_name = "products"
    queryset = Products.objects.filter(state=True)


class NewsTemplateView(TemplateView):
    template_name = "products/news.html"


class GalleryTemplateView(ListView):
    model = Products
    context_object_name = "products"
    template_name = "products/gallery.html"


class ProductDetailView(DetailView):
    template_name = "products/product_info.html"
    model = Products


class CreateProduct(CreateView):
    template_name = "products/create_product.html"
    form_class = ProductsForm

    def get_success_url(self) -> str:
        return reverse_lazy("product_info", kwargs={"pk": self.object.pk})


class DeleteProduct(DeleteView):
    model = Products
    template_name = "products/products_confirm_delete.html"

    def get_success_url(self) -> str:
        return reverse_lazy("menu") + "?ok"


class UpdateProduct(UpdateView):
    model = Products
    form_class = ProductsForm
    template_name = "products/update_product.html"

    def get_success_url(self) -> str:
        return reverse_lazy("product_info", args=[self.object.id]) + "?updated"
