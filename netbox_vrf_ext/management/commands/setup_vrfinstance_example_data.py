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
            manu_obj = Manufacturer.object.get(
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
            devrole_obj = DeviceRole.object.get(
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
            site_obj = Site.object.get(
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
                type=devicetype_obj,
                site=site_obj,
                status="active"
            )
            for x in range(0,3):
                int_obj = Interface.objects.create(
                    device=device_obj,
                    name=f"et-0/0/{x}",
                    type="100gbase-x-qsfp28",

                )

        ipaddress_object_type = ObjectType.objects.get_for_model(IPAddress)
        prefix_object_type = ObjectType.objects.get_for_model(Prefix)

        if options["remove"]:
            try:
                CustomField.objects.get(
                    name="prefix_vrfinstance", object_types=prefix_object_type
                ).delete()
                if options.get("verbose"):
                    self.stdout.write("Custom field prefix_vrfinstance removed")
            except CustomField.DoesNotExist:
                pass
            try:
                CustomField.objects.get(
                    name="ipaddress_vrfinstance", object_types=ipaddress_object_type
                ).delete()
                if options.get("verbose"):
                    self.stdout.write("Custom field ipaddress_vrfinstance removed")
            except CustomField.DoesNotExist:
                pass
        else:
            vrfinstance_object_type = ObjectType.objects.get_for_model(VRFInstance)
            if not CustomField.objects.filter(
                name="ipaddress_vrfinstance",
                type=CustomFieldTypeChoices.TYPE_OBJECT,
                object_types=ipaddress_object_type
            ).exists():
                cf_name = CustomField.objects.create(
                    name="ipaddress_vrfinstance",
                    label="VRF Instance",
                    type=CustomFieldTypeChoices.TYPE_OBJECT,
                    related_object_type=vrfinstance_object_type,
                    required=False,
                )
                cf_name.object_types.set([ipaddress_object_type])
                if options.get("verbose"):
                    self.stdout.write(
                        "Created custom field 'ipaddress_vrfinstance'"
                    )
            if not CustomField.objects.filter(
                name="prefix_vrfinstance",
                type=CustomFieldTypeChoices.TYPE_OBJECT,
                object_types=prefix_object_type
            ).exists():
                cf_name = CustomField.objects.create(
                    name="prefix_vrfinstance",
                    label="VRF Instance",
                    type=CustomFieldTypeChoices.TYPE_OBJECT,
                    related_object_type=vrfinstance_object_type,
                    required=False,
                )
                cf_name.object_types.set([prefix_object_type])
                if options.get("verbose"):
                    self.stdout.write(
                        "Created custom field 'prefix_vrfinstance'"
                    )

