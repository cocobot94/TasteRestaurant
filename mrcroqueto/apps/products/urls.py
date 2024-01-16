from django.urls import path
from apps.products.views import (
    ListProducts,
    MenuListView,
    NewsTemplateView,
    GalleryTemplateView,
    ProductDetailView,
    CreateProduct,
    DeleteProduct,
    UpdateProduct,
    OrderView,
    OrderCreate,
    DetailCreate,
)


urlpatterns = [
    path("offers/", ListProducts.as_view(), name="offers"),
    path("menu/", MenuListView.as_view(), name="menu"),
    path("news/", NewsTemplateView.as_view(), name="news"),
    path("gallery/", GalleryTemplateView.as_view(), name="gallery"),
    path("product_info/<int:pk>/", ProductDetailView.as_view(), name="product_info"),
    path("product_create/", CreateProduct.as_view(), name="create_product"),
    path("delete/<int:pk>/", DeleteProduct.as_view(), name="delete_product"),
    path("update/<int:pk>/", UpdateProduct.as_view(), name="update_product"),
    path("order/<int:pk>/", OrderView.as_view(), name="order"),
    path("order/create/", OrderCreate.as_view(), name="order_create"),
    path("order/detail_create/", DetailCreate.as_view(), name="detail_create"),
]
