import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn

from .models import netbox_vrf_ext


class netbox_vrf_extTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = netbox_vrf_ext
        fields = ("pk", "id", "name", "actions")
        default_columns = ("name",)
