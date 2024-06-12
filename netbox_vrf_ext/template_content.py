from netbox.plugins import PluginTemplateExtension


class AddInstanceButton(PluginTemplateExtension):
    model = "ipam.vrf"

    def buttons(self):
        return self.render("netbox_vrf_ext/inc/vrf_add_button.html")


template_extensions = [AddInstanceButton]
