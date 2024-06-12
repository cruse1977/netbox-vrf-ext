from netbox.api.viewsets import NetBoxModelViewSet
from ..models import VRFInstance
from .serializers import VRFInstanceSerializer


class VRFInstanceViewSet(NetBoxModelViewSet):
    queryset = VRFInstance.objects.prefetch_related('tags')
    serializer_class = VRFInstanceSerializer
