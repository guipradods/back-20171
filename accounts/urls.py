from django.conf.urls import url

from .views import (
    login_user,
    logout_user,
)

urlpatterns = [
    url(r'^login/$', login_user, name='login_user'),
    url(r'^logout/$', logout_user, name='logout_user'),
]
