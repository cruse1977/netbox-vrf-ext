from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

plugin_buttons = [
    PluginMenuButton(
        link="plugins:netbox_vrf_ext:netboxvrfext_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
    )
]

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_vrf_ext:netboxvrfext_list",
        link_text="netbox_vrf_ext",
        buttons=plugin_buttons,
    ),
)
