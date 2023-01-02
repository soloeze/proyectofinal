from django.urls import path
#from .views import home,TareaList
from AppCoder import views
#from AppCoder import views
urlpatterns = [
    path('', views.home, name='home'),
    path('tarea/list/',views.TareaList.as_view(),name='listar_tarea' ),
    path('tarea/create/',views.TareaCreacion.as_view(),name='crear_tarea' ),
    path('tarea/edit/<pk>',views.TareaEdit.as_view(),name='editar_tarea' ),
    path('tarea/remove/<pk>',views.TareaDelete.as_view(),name='eliminar_tarea' ),
    path('tarea/detail/<pk>',views.TareaDetail.as_view(),name='detalle_tarea' ),
    path('tarea/busquedanombretarea/', views.buscarTarea, name='busqueda_tarea'),
    path('tarea/buscar/', views.buscarResultadoTarea),
    path('personasdelequipo/list/',views.PersonasDelEquipoList.as_view(),name='listar_pde' ),
    path('personasdelequipo/create/',views.PersonasDelEquipoCreacion.as_view(),name='crear_pde' ),
    path('personasdelequipo/edit/<pk>',views.PersonasDelEquipoEdit.as_view(),name='editar_pde' ),
    path('personasdelequipo/remove/<pk>',views.PersonasDelEquipoDelete.as_view(),name='eliminar_pde' ),
    path('personasdelequipo/detail/<pk>',views.PersonasDelEquipoDetail.as_view(),name='detalle_pde' ),
    path('personasdelequipo/busquedanombrepde/', views.buscarPersonasDelEquipo, name='busqueda_pde'),
    path('personasdelequipo/buscar/', views.buscarResultadoPersonasDelEquipo),
    path('contacto/list/',views.ContactoList.as_view(),name='listar_contacto' ),
    path('contacto/create/',views.ContactoCreacion.as_view(),name='crear_contacto' ),
    path('contacto/edit/<pk>',views.ContactoEdit.as_view(),name='editar_contacto' ),
    path('contacto/remove/<pk>',views.ContactoDelete.as_view(),name='eliminar_contacto' ),
    path('contacto/detail/<pk>',views.ContactoDetail.as_view(),name='detalle_contacto' ),
    path('contacto/busquedanombrecontacto/', views.buscarContacto, name='busqueda_contacto'),
    path('contacto/buscar/', views.buscarResultadoContacto),
    path('registro/', views.registro,name='registro'),
]