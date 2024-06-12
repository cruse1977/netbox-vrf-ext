from dcim.models import Device, DeviceRole, DeviceType, Manufacturer, Site
from ipam.models import VRF
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from rest_framework import status
from utilities.testing import APITestCase, APIViewTestCases

from netbox_vrf_ext.models import *

"""Tests for `netbox_vrf_ext` package."""

class AppTest(APITestCase):
    def test_root(self):
        url = reverse("plugins-api:netbox_vrf_ext-api:api-root")
        response = self.client.get(f"{url}?format=api", **self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ACLTestCase(APIViewTestCases.APIViewTestCase):
    """Test the AccessList Test"""

    model = VRFInstance
    view_namespace = "plugins-api:netbox_vrf_ext"
    brief_fields = ["display", "id", "name", "url"]

    @classmethod
    def setUpTestData(cls):
        site = Site.objects.create(name="Site 1", slug="site-1")
        manufacturer = Manufacturer.objects.create(
            name="Manufacturer 1",
            slug="manufacturer-1",
        )
        devicetype = DeviceType.objects.create(
            manufacturer=manufacturer,
            model="Device Type 1",
        )
        devicerole = DeviceRole.objects.create(
            name="Device Role 1",
            slug="device-role-1",
        )
        device = Device.objects.create(
            name="Device 1",
            site=site,
            device_type=devicetype,
            role=devicerole,
        )

        vrf_1 = VRF.objects.create(
            name="Test 1",
            rd="1:1"
        )

        vrf_2 = VRF.objects.create(
            name="Test 2",
            rd="2:2"
        )

        vrf_instances = (
            VRFInstance(
                vrf = vrf_1.id,
                device=device.id
            ),
            VRFInstance(
                vrf = vrf_2.id,
                device=device.id
            ),
        )
        
        VRFInstance.objects.bulk_create(vrf_instances)

        cls.create_data = [
            {
                "device": device.id,
                "vrf": vrf.id
            },
        ]

