from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("netbox-vrf-exts/", views.netbox_vrf_extListView.as_view(), name="netboxvrfext_list"),
    path("netbox-vrf-exts/add/", views.netbox_vrf_extEditView.as_view(), name="netboxvrfext_add"),
    path("netbox-vrf-exts/<int:pk>/", views.netbox_vrf_extView.as_view(), name="netboxvrfext"),
    path("netbox-vrf-exts/<int:pk>/edit/", views.netbox_vrf_extEditView.as_view(), name="netboxvrfext_edit"),
    path("netbox-vrf-exts/<int:pk>/delete/", views.netbox_vrf_extDeleteView.as_view(), name="netboxvrfext_delete"),
    path(
        "netbox-vrf-exts/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="netboxvrfext_changelog",
        kwargs={"model": models.netbox_vrf_ext},
    ),
)
