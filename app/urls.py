from django.urls import path, include
from rest_framework import routers

from .views import NavigationSafetyObjectViewSet

router = routers.DefaultRouter()
router.register('navigation-safety-object', NavigationSafetyObjectViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]       