from django.conf.urls import url,include
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^crudfinal/(?P<pk>[0-9]+)/$', views.post_detail),
#En la terminal se indica que esta linea ya no es indispensable para el funcionamiento
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),


    #para editar, guardar y eliminar fotos
#    url(r'^photo/(?P<pk>\d+)/update/$', views.PhotoUpdate.as_view(), name='photo-update'),
    #Create
#    url(r'^photo/create/$', views.PhotoCreate.as_view(), name='photo-create'),
    #Delete
#   url(r'^photo/(?P<pk>\d+)/delete/$', views.PhotoDelete.as_view(), name='photo-delete'),

]
