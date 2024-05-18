"""Top-level package for NetBox VRF Extensions."""

__author__ = """Chris Russell"""
__email__ = "cruse1977123@gmail.com"
__version__ = "0.1.0"


from netbox.plugins import PluginConfig


class netbox_vrf_extConfig(PluginConfig):
    name = "netbox_vrf_ext"
    verbose_name = "NetBox VRF Extensions"
    description = "Netbox Plugin Extending VRF Support"
    version = "version"
    base_url = "netbox_vrf_ext"


config = netbox_vrf_extConfig
