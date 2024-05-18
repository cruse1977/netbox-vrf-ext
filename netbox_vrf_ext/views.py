from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


class netbox_vrf_extView(generic.ObjectView):
    queryset = models.netbox_vrf_ext.objects.all()


class netbox_vrf_extListView(generic.ObjectListView):
    queryset = models.netbox_vrf_ext.objects.all()
    table = tables.netbox_vrf_extTable


class netbox_vrf_extEditView(generic.ObjectEditView):
    queryset = models.netbox_vrf_ext.objects.all()
    form = forms.netbox_vrf_extForm


class netbox_vrf_extDeleteView(generic.ObjectDeleteView):
    queryset = models.netbox_vrf_ext.objects.all()
