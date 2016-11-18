from django.conf.urls import url,include
from . import views
from django.conf import settings
urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^crudfinal/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),

]
