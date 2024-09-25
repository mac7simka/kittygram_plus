from rest_framework.routers import DefaultRouter

from django.urls import include, path

from cats.views import CatViewSet, OwnerViewSet


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)

urlpatterns = [
    path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
