from django.conf.urls import url, include

urlpatterns = (
    url(r'^auth/', include('scpc_auth.api.urls', namespace='auth')),
)