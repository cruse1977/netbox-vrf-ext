"""Top-level package for NetBox VRF Extensions."""
from netbox.plugins import PluginConfig
from .version import __version__


class VRFExtConfig(PluginConfig):
    name = 'netbox_vrf_ext'
    verbose_name = 'netbox_vrf_ext'
    description = 'extended vrf related objects'
    version = __version__
    author = 'Chris Russell'
    author_email = 'cruse1977123@gmail.com'
    base_url = 'vrf-ext'
    required_settings = []
    min_version = '4.0.2'
    max_version = '4.0.99'
    default_settings = {
        'device_ext_page': 'right',
        'top_level_menu' : False,
    }

config = VRFExtConfig 
