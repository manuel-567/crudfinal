from django.conf.urls import url,include
from . import views
from django.conf import settings
urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),


]
