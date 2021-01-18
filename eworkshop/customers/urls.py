from rest_framework import routers

from .views import customers, devices, contacts

router = routers.SimpleRouter()
router.register(
    r'(?P<client_id>[0-9]+)/contacts', contacts.ContactViewSet, basename='contacts')
router.register(r'devices', devices.DeviceViewSet)
router.register('', customers.CustomerViewSet)


urlpatterns = router.urls
