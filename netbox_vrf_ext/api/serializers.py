from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from netbox.api.fields import SerializedPKRelatedField
from ..models import *
from dcim.api.serializers import NestedDeviceSerializer
from ipam.api.nested_serializers import NestedRouteTargetSerializer
from ipam.api.serializers import NestedVRFSerializer
from django.utils.translation import gettext_lazy as _
from ipam.models import RouteTarget


class VRFInstanceSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_vrf_ext-api:vrfinstance-detail'
    )
    device = NestedDeviceSerializer()
    vrf = NestedVRFSerializer()
    import_targets = SerializedPKRelatedField(
        queryset=RouteTarget.objects.all(),
        serializer=NestedRouteTargetSerializer,
        required=False,
        many=True
    )
    export_targets = SerializedPKRelatedField(
        queryset=RouteTarget.objects.all(),
        serializer=NestedRouteTargetSerializer,
        required=False,
        many=True
    )

    class Meta:
        model = VRFInstance
        fields = (
            'id', 'url', 'display', 'vrf', 'device', 'rd',
            'import_targets', 'export_targets', 'tags',
            'custom_fields', 'created', 'last_updated',
        )
