from django.conf.urls import url

from scpc_auth.api import views

urlpatterns = (
    url(r'^register-by-email/$', views.EmailRegistrationAPIView.as_view(), name='register_by_email'),
    url(r'^login-by-email/$', views.EmailLoginAPIView.as_view(), name='login_by_email'),
)