from django.core.management.base import BaseCommand

from core.models import ObjectType
from extras.models import CustomField
from extras.choices import CustomFieldTypeChoices
from ipam.models import IPAddress, Prefix
from dcim.models import Interface
from netbox_vrf_ext.models import VRFInstance

# thanks to Peter Enkel of netbox-plugin-dns for this example
class Command(BaseCommand):
    help = "Setup VRFInstance fields on Prefix, IP Address to mirror VRF"

    def add_arguments(self, parser):
        parser.add_argument(
            "--remove", action="store_true", help="Remove custom fields"
        )
        parser.add_argument("--verbose", action="store_true", help="Verbose output")

    def handle(self, *model_names, **options):
        ipaddress_object_type = ObjectType.objects.get_for_model(IPAddress)
        prefix_object_type = ObjectType.objects.get_for_model(Prefix)
        interface_object_type = ObjectType.objects.get_for_model(Interface)
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
            try:
                CustomField.objects.get(
                    name="interface_vrfinstance", object_types=interface_object_type
                ).delete()
                if options.get("verbose"):
                    self.stdout.write("Custom field interface_vrfinstance removed")
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

            if not CustomField.objects.filter(
                name="interface_vrfinstance",
                type=CustomFieldTypeChoices.TYPE_OBJECT,
                object_types=interface_object_type
            ).exists():
                cf_name = CustomField.objects.create(
                    name="interface_vrfinstance",
                    label="VRF Instance",
                    type=CustomFieldTypeChoices.TYPE_OBJECT,
                    related_object_type=vrfinstance_object_type,
                    required=False,
                )
                cf_name.object_types.set([interface_object_type])
                if options.get("verbose"):
                    self.stdout.write(
                        "Created custom field 'interface_vrfinstance'"
                    )
