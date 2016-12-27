from django.conf.urls import url

from scpc_location.api import views

urlpatterns = (
    url(r'^$', views.UpdateUserLocationView.as_view(), name='register_location'),
)