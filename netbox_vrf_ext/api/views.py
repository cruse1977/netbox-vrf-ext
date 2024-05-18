from netbox.api.viewsets import NetBoxModelViewSet
from ..models import *
from .serializers import *

class VRFInstanceViewSet(NetBoxModelViewSet):
    queryset = VRFInstance.objects.prefetch_related('tags')
    serializer_class = VRFInstanceSerializer


