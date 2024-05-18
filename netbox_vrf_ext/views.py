from .forms import VRFInstanceForm
from .models import VRFInstance
from .tables import VRFInstanceTable
from dcim.models import Device
from ipam.tables import RouteTargetTable
from netbox.views import generic
from utilities.views import ViewTab, register_model_view


class VRFInstanceView(generic.ObjectView):
    queryset = VRFInstance.objects.all()
    def get_extra_context(self, request, instance):
        import_targets_table = RouteTargetTable(
            instance.import_targets.all(),
            orderable=False
        )
        export_targets_table = RouteTargetTable(
            instance.export_targets.all(),
            orderable=False
        )

        return {
            'import_targets_table': import_targets_table,
            'export_targets_table': export_targets_table,
        }

class VRFInstanceListView(generic.ObjectListView):
    queryset = VRFInstance.objects.all()
    table = VRFInstanceTable

class VRFInstanceEditView(generic.ObjectEditView):
    queryset = VRFInstance.objects.all()
    form = VRFInstanceForm

class VRFInstanceDeleteView(generic.ObjectDeleteView):
    queryset = VRFInstance.objects.all()

@register_model_view(Device, 'devicevrfinstanceview', path='vrfinstances')
class DeviceVRFInstanceView(generic.ObjectChildrenView):
    queryset = Device.objects.all()
    child_model = VRFInstance
    table = VRFInstanceTable
    template_name = "netbox_vrf_ext/vrfinstance_tab.html"
    ...
    tab = ViewTab(
        label='VRF Instances',
        badge=lambda obj: VRFInstance.objects.filter(device=obj).count(),
        hide_if_empty=True
    )


    def get_children(self, request, parent):
        return VRFInstance.objects.filter(
            device=parent
        )