from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import views, models

urlpatterns = (
    path('vrfinstance/', views.VRFInstanceListView.as_view(), name = "vrfinstance_list"),
    path('vrfinstance/add', views.VRFInstanceEditView.as_view(), name = "vrfinstance_add"),
    path('vrfinstance/<int:pk>', views.VRFInstanceView.as_view(), name = "vrfinstance"),
    path('vrfinstance/<int:pk>/edit', views.VRFInstanceEditView.as_view(), name = "vrfinstance_edit"),
    path('vrfinstance/<int:pk>/delete', views.VRFInstanceDeleteView.as_view(), name = "vrfinstance_delete"),    
    path('vrfinstance/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='vrfinstance_changelog', kwargs={
        'model': models.VRFInstance
    }),
)