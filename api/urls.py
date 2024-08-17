from django.urls import path, include
from rest_framework import routers
from .views import LeadViewSet, OrigemViewSet

router = routers.DefaultRouter()
router.register(r'leads', LeadViewSet)
router.register(r'origens', OrigemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
