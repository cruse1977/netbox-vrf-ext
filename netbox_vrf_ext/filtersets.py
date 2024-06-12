#from netbox.filtersets import NetBoxModelFilterSet
#from .models import netbox_vrf_ext


# class netbox_vrf_extFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = netbox_vrf_ext
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
