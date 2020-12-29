from rest_framework import routers


from .views import *

router = routers.SimpleRouter()
router.register(r'products', products.ProductViewSet)
router.register(r'spare_parts', spareparts.SparePartViewSet)
router.register(r'spare_parts_types', sparepart_types.SparePartTypeViewSet)
router.register(r'brands', brands.BrandViewSet)
router.register(r'device_models', device_models.DeviceModelViewSet)
router.register(r'device_types', device_types.DeviceTypeViewSet)


urlpatterns = router.urls
