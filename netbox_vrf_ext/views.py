from .forms import VRFInstanceForm
from .models import VRFInstance
from .tables import VRFInstanceTable
from dcim.models import Device
from ipam.models import Prefix, IPAddress, VRF
from ipam.tables import RouteTargetTable
from netbox.views import generic
from utilities.views import ViewTab, register_model_view
from extras.models import CustomField

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
        # try to grab both our custom fields 
        pcf_obj = CustomField.objects.filter(
            name = "prefix_vrfinstance"
        )
        ipcf_obj = CustomField.objects.filter(
                name = "ipaddress_vrfinstance"
            )
        if pcf_obj and ipcf_obj:
            related_models = (
                (Prefix.objects.restrict.filter(cf_prefix_vrfinstance=instance), 'vrf_id'),
                (IPAddress.objects.restrict.filter(cf_ipaddress_vrfinstance=instance), 'vrf_id'),
            )
        else:
            related_models = None

        return {
            'import_targets_table': import_targets_table,
            'export_targets_table': export_targets_table,
            'related_models': related_models
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
    
@register_model_view(VRF, 'vrfvrfinstanceview', path='vrfinstances')
class VRFVRFInstanceView(generic.ObjectChildrenView):
    queryset = VRF.objects.all()
    child_model = VRFInstance
    table = VRFInstanceTable
    template_name = "netbox_vrf_ext/vrfinstance_tab.html"
    ...
    tab = ViewTab(
        label='VRF Instances',
        badge=lambda obj: VRFInstance.objects.filter(vrf=obj).count(),
        hide_if_empty=True
    )


    def get_children(self, request, parent):
        return VRFInstance.objects.filter(
            vrf=parent
        )
    
