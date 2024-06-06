from netbox.plugins import PluginMenu, PluginMenuButton, PluginMenuItem

vrfinstance_mi = PluginMenuItem(
    link='plugins:netbox_vrf_ext:vrfinstance_list',
    link_text='VRF Instance',
    buttons=(
        PluginMenuButton(
            link='plugins:netbox_vrf_ext:vrfinstance_add',
            title='VRF Instance Add',
            icon_class='mdi mdi-plus-thick'),
    )
)

menu = PluginMenu(
    label='VRF extensions',
    groups=(
            (
                'Components', (vrfinstance_mi,),
            ),
        ),
    icon_class='mdi mdi-circle-double'
)
