# NetBox VRF Extensions

Netbox Plugin Extending VRF Support


* Free software: MIT
* Documentation: https://cruse1977.github.io/netbox-vrf-ext/


## Features

Provides an extension to VRF with the ability to define an instance to a specific device, overriding RD/RTs. 

## Compatibility

| NetBox Version | Plugin Version |
|----------------|----------------|
|     4.0.2      |      0.1.0     |

## Installing

For adding to a NetBox Docker setup see
[the general instructions for using netbox-docker with plugins](https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins).

While this is still in development and not yet on pypi you can install with pip:

```bash
pip install git+https://github.com/cruse1977/netbox-vrf-ext
```

or by adding to your `local_requirements.txt` or `plugin_requirements.txt` (netbox-docker):

```bash
git+https://github.com/cruse1977/netbox-vrf-ext
```

Enable the plugin in `/opt/netbox/netbox/netbox/configuration.py`,
 or if you use netbox-docker, your `/configuration/plugins.py` file :

```python
PLUGINS = [
    'netbox_vrf_ext'
]

PLUGINS_CONFIG = {
    "netbox-vrf-ext": {},
}
```

## Credits

Based on the NetBox plugin tutorial:

- [demo repository](https://github.com/netbox-community/netbox-plugin-demo)
- [tutorial](https://github.com/netbox-community/netbox-plugin-tutorial)

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`netbox-community/cookiecutter-netbox-plugin`](https://github.com/netbox-community/cookiecutter-netbox-plugin) project template.
