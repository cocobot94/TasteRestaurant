from rest_framework.routers import DefaultRouter
from apps.api.views.user_view import UserViewSet
from apps.api.views.product_views import ProductViewSet


router = DefaultRouter()
router.register(r"users", viewset=UserViewSet, basename="users")
router.register(r"products", viewset=ProductViewSet, basename="products")

urlpatterns = router.urls
