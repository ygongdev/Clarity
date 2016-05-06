from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^resources/$', views.resources, name='resources'),
    url(r'^communication/$', views.communication, name='communication'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^add_info/$', views.add_info, name='add_info'),
    url(r'^delete_info/(?P<info_id>[0-9]+)/$', views.delete_info, name='delete_info'),

]