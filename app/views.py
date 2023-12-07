from rest_framework import viewsets

from .models import NavigationSafetyObjectModel
from .serializers import NavigationSafetyObjectSerializer

class NavigationSafetyObjectViewSet(viewsets.ModelViewSet):
    queryset = NavigationSafetyObjectModel.objects.all()
    serializer_class = NavigationSafetyObjectSerializer