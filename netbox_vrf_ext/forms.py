from django.utils.translation import gettext_lazy as _
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import DynamicModelChoiceField, DynamicModelMultipleChoiceField, CommentField
from dcim.models import Device
from ipam.models import RouteTarget, VRF
from .models import VRFInstance


class VRFInstanceForm(NetBoxModelForm):

    import_targets = DynamicModelMultipleChoiceField(
        label=_('Import targets'),
        queryset=RouteTarget.objects.all(),
        query_params={
            'vrf_id': '$vrf',
            'fields': 'import_targets'
        },
        required=False
    )
    export_targets = DynamicModelMultipleChoiceField(
        label=_('Export targets'),
        queryset=RouteTarget.objects.all(),
        query_params={
            'vrf_id': '$vrf',
            'fields': 'export_targets'
        },
        required=False
    )

    device = DynamicModelChoiceField(
        queryset=Device.objects.all()
    )

    vrf = DynamicModelChoiceField(
        queryset=VRF.objects.all()
    )
    comments = CommentField()

    fieldsets = (
        (_('Applied Device'), ('device',)),
        (_('VRF'), ('vrf', 'rd', )),
        (_('Route Targets'), ('import_targets', 'export_targets',)),
        (_('tenant'), ('tenant',)),
        (_('Metadata'), ('tags',)),
    )

    class Meta:
        model = VRFInstance
        fields = [
            'vrf', 'rd',
            'device',
            'import_targets', 'export_targets',
            'tenant',
            'tags',
            'comments'
        ]
