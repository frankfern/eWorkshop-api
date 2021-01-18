from rest_framework import routers


from .views import *

router = routers.SimpleRouter()
router.register(r'sells', SellServiceViewSet)
router.register(r'service_products', ServiceProductViewSet)
# router.register(
#     r'sells/(?P<service_id>[0-9]+)/products', ServiceProductViewSet, basename='products')
router.register(r'fixing_service', FixServiceViewSet)
router.register(r'service_type', ServiceTypeViewSet)


urlpatterns = router.urls
