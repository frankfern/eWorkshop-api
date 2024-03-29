from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),

    path('api/v1/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),

    path('api/v1/', include('eworkshop.staff.urls')),
    path('api/v1/suppliers/', include('eworkshop.suppliers.urls')),
    path('api/v1/customers/', include('eworkshop.customers.urls')),
    path('api/v1/stock/', include('eworkshop.stock.urls')),
    path('api/v1/services/', include('eworkshop.services.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
