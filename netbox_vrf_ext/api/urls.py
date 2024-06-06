from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_vrf_ext'

router = NetBoxRouter()
router.register('vrfinstance', views.VRFInstanceViewSet)
urlpatterns = router.urls
