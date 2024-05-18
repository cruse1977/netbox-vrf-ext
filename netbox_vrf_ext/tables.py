import django_tables2 as tables
from django.utils.translation import gettext_lazy as _
from netbox.tables import NetBoxTable, TemplateColumn
from .models import VRFInstance

class RelatedVRFInstanceTable(NetBoxTable):

    class Meta(NetBoxTable.Meta):
        model = VRFInstance
        fields = ('pk','id','rd', 'device')

VRF_TARGETS = """
{% for rt in value.all %}
  <a href="{{ rt.get_absolute_url }}">{{ rt }}</a>{% if not forloop.last %}<br />{% endif %}
{% endfor %}
"""


class VRFInstanceTable(NetBoxTable):

    vrf = tables.Column(
        linkify=True
    )
    device = tables.Column(
        linkify=True
    )
    rd = tables.Column(
        verbose_name=_('RD')
    )

    import_targets = TemplateColumn(
        verbose_name=_('Import Targets'),
        template_code=VRF_TARGETS,
        orderable=False
    )
    export_targets = TemplateColumn(
        verbose_name=_('Export Targets'),
        template_code=VRF_TARGETS,
        orderable=False
    )

    class Meta(NetBoxTable.Meta):
        model = VRFInstance
        fields = ('pk', 'id', 'tenant', 'vrf', 'rd', 'import_targets', 'export_targets', 'device')
        default_columns = ('id', 'vrf', 'device')