from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('proyecto/nuevo/', views.crear_proyecto, name='agregar_proyecto'),

    path('tester/nuevo/', views.crear_tester, name='agregar_tester'),

    path('caso/nuevo/', views.crear_caso, name='crear_caso'),
    path('caso/<int:pk>/', views.detalle_caso, name='detalle_caso'),
    path('caso/buscar/', views.buscar_caso, name='buscar_caso'),

    path('casos/', views.lista_casos, name='lista_casos'),
]
