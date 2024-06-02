from django.core.management.base import BaseCommand
from dcim.models import Device, Manufacturer, DeviceRole, DeviceType, Interface, Site
from core.models import ObjectType
from extras.models import CustomField
from extras.choices import CustomFieldTypeChoices
from ipam.models import IPAddress, Prefix
from netbox_vrf_ext.models import VRFInstance

# thanks to Peter Enkel of netbox-plugin-dns for this example
class Command(BaseCommand):
    help = "Creates VRF Instance Sample Data"

    def add_arguments(self, parser):
        #    "--remove", action="store_true", help="Remove custom fields"
        ##parser.add_argument(
        #)
        parser.add_argument("--verbose", action="store_true", help="Verbose output")

    def handle(self, *model_names, **options):
        # create a sample device - Juniper MX204

        # manufacturer
        if not Manufacturer.objects.filter(
                name="Juniper"
        ).exists():
                manu_obj = Manufacturer.objects.create(
                    name="Juniper",
                    slug="manu_juniper",
                )
        else:
            manu_obj = Manufacturer.objects.get(
                name="Juniper",
                slug="manu_juniper",
            )

        # Device Role
        if not DeviceRole.objects.filter(
                name="router"
        ).exists():
                devrole_obj = DeviceRole.objects.create(
                    name="router",
                    slug="devrole_router",
                )
        else:
            devrole_obj = DeviceRole.objects.get(
                name="router",
            )

        if not Site.objects.filter(
                name="Site1"
        ).exists():
                site_obj = Site.objects.create(
                    name="Site1",
                    slug="site_site1",
                    status="active",
                )
        else:
            site_obj = Site.objects.get(
                name="Site1",
            )
        if not DeviceType.objects.filter(
                model="MX204"
        ).exists():       
            devicetype_obj = DeviceType.objects.create(
                manufacturer = manu_obj,
                model="MX204",
                slug="devtype_mx204",
            )
        else:
             devicetype_obj = DeviceType.objects.get(
                  model="MX204"
             )
        if not Device.objects.filter(
                name="Router1"
        ).exists():
            device_obj = Device.objects.create(
                name="Router1",
                role=devrole_obj,
                device_type=devicetype_obj,
                site=site_obj,
                status="active"
            )
            for x in range(0,3):
                int_obj = Interface.objects.create(
                    device=device_obj,
                    name=f"et-0/0/{x}",
                    type="100gbase-x-qsfp28",

                )
        if not Device.objects.filter(
                name="Router2"
        ).exists():
            device_obj = Device.objects.create(
                name="Router2",
                role=devrole_obj,
                device_type=devicetype_obj,
                site=site_obj,
                status="active"
            )
            for x in range(0,3):
                int_obj = Interface.objects.create(
                    device=device_obj,
                    name=f"et-0/0/{x}",
                    type="100gbase-x-qsfp28",

                )
        if not Device.objects.filter(
                name="Router3"
        ).exists():
            device_obj = Device.objects.create(
                name="Router3",
                role=devrole_obj,
                device_type=devicetype_obj,
                site=site_obj,
                status="active"
            )
            for x in range(0,3):
                int_obj = Interface.objects.create(
                    device=device_obj,
                    name=f"et-0/0/{x}",
                    type="100gbase-x-qsfp28",

                )




