from rest_framework import routers

from .views import customers, devices, contacts

router = routers.SimpleRouter()
router.register(r'contacts', contacts.ContactViewSet)
router.register(r'devices', devices.DeviceViewSet)
router.register('', customers.CustomerViewSet)


urlpatterns = router.urls
