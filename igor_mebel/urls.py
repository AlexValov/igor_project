from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from shop.views import CategoryViewSet, ProductViewSet
from .yasg import urlpatterns as doc_urls


router = routers.DefaultRouter()
router.register('api/category', CategoryViewSet)
router.register('api/product', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += doc_urls
urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
