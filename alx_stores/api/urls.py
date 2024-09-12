from rest_framework.routers import DefaultRouter
from api.products.views import ProductViewSet

router = DefaultRouter()
router.register('', ProductViewSet, basename='product')
urlpatterns = router.urls