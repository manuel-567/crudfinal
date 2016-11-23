from django.conf.urls import url,include
from . import views
from django.conf import settings


urlpatterns = [
#para el manejo de los archivos multimedia en este caso seran las fotos
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
#para trabajar el home y las opciones de la pagina principal
    url(r'^home/$', views.post_list),
    url(r'^home/detalles/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^home/nuevo/$', views.post_new, name='post_new'),
    url(r'^home/detalles/(?P<pk>[0-9]+)/editar/$', views.post_edit, name='post_edit'),
    url(r'^home/detalle/(?P<pk>[0-9]+)/eliminar$', views.post_delete, name='post_delete'),
#para trabajar las categorias

    url(r'^home/listar/categorias/$', views.post_list_categoria, name='post_list_categoria'),
    url(r'^home/listar/categorias/nueva/$', views.post_new_categoria, name='post_new_categoria'),
    url(r'^home/listar/categorias/detalle/(?P<pk>[0-9]+)/editar/$', views.post_edit_categoria, name='post_edit_categoria'),
    url(r'^home/listar/categoria/detalle/(?P<pk>[0-9]+)/$', views.post_detail_categoria),
    url(r'^home/listar/categoria/detalle/(?P<pk>[0-9]+)/eliminar$', views.post_delete_categoria, name='post_delete_categoria'),




#    url(r'^post/categoria/$', views.nueva_categoria, name='nueva_categoria'),
#    url(r'^post/categoria/(?P<pk>[0-9]+)/editar/$', views.editar_categoria, name='editar_categoria'),

]
