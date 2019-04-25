from django.conf.urls import url

from .views import (
    CourseList,
    CourseDetail,
    CourseCreation,
    CourseUpdate,
    CourseDelete,
    CajaList,
    CajaDetail,
    CajaCreation,
    CajaUpdate,
    CajaDelete,
    ProductoDetail,
    ProductoCreation,
    ProductoUpdate,
    ProductoDelete
)

urlpatterns = [

    url(r'^$', CourseList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', CourseDetail.as_view(), name='detail'),
    url(r'^nuevo$', CourseCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', CourseUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', CourseDelete.as_view(), name='delete'),
    url(r'^nuevaCaja$', CajaCreation.as_view(), name='new1'),
    url(r'^editarCaja/(?P<pk>\d+)$', CajaUpdate.as_view(), name='edit1'),
    url(r'^borrarCaja/(?P<pk>\d+)$', CajaDelete.as_view(), name='delete1'),
    url(r'^caja/(?P<pk>\d+)$', CajaDetail.as_view(), name='detail1'),
    url(r'^nuevoProducto$', ProductoCreation.as_view(), name='new2'),
    url(r'^editarProducto/(?P<pk>\d+)$', ProductoUpdate.as_view(), name='edit2'),
    url(r'^borrarProducto/(?P<pk>\d+)$', ProductoDelete.as_view(), name='delete2'),
    url(r'^producto/(?P<pk>\d+)$', ProductoDetail.as_view(), name='detail2'),
]