from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db import models
from netbox.models import NetBoxModel

class VRFInstance(NetBoxModel):
    """
      VRFInstance models an instance of a VRF on a Device
    """
    
    vrf = models.ForeignKey(
        to='ipam.VRF',
        on_delete=models.CASCADE,
        related_name="%(class)s_related",
    )
    
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.CASCADE,
        related_name="%(class)s_related",
    )

    # may/may not be weird - Cisco often uses a loopback w/ips,
    # junos doesn't require an ip on the interface but does the interface itself
    # either way, not mandatory 
    loopback_interface = models.ForeignKey(
        to='dcim.Interface',
        on_delete=models.PROTECT,
        related_name="%(class)s_related",
        blank=True,
        null=True
    )

    rd = models.CharField(
        max_length=21,
        unique=True,
        blank=True,
        null=True,
        verbose_name=_('route distinguisher'),
        help_text=_('Unique route distinguisher (as defined in RFC 4364)')
    )

    import_targets = models.ManyToManyField(
        to='ipam.RouteTarget',
        related_name='instance_importing_vrfs',
        blank=True
    )
    export_targets = models.ManyToManyField(
        to='ipam.RouteTarget',
        related_name='instance_exporting_vrfs',
        blank=True
    )

    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
        related_name='tenants'
    )


    description = models.CharField(
        max_length=200,
        blank=True
    )

    class Meta:
        verbose_name = 'VRF Instance'
        verbose_name_plural = 'VRF Instances'
        unique_together = ['vrf', 'device']

    def __str__(self):
        return f"{self.vrf}:{self.device}"

    def get_absolute_url(self):
        return reverse('plugins:netbox_vrf_ext:vrfinstance', args=[self.pk])
    
