from eworkshop.services.views.fix_sparepart import FixSparepartViewset
from rest_framework import routers


from .views import *

router = routers.SimpleRouter()
router.register(r'sells', SellServiceViewSet)
router.register(r'fixing_service', FixServiceViewSet)
router.register(
    r'sells/(?P<service_id>[0-9]+)/spareparts', FixSparepartViewset, basename='products')
router.register(r'service_type', ServiceTypeViewSet)


urlpatterns = router.urls
