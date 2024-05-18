from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import netbox_vrf_ext


class netbox_vrf_extForm(NetBoxModelForm):
    class Meta:
        model = netbox_vrf_ext
        fields = ("name", "tags")
