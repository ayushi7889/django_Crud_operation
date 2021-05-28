from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Crud_form,name='employee_insert'),
    path('<int:id>/', views.Crud_form,name='employee_update'),
    path('delete/<int:id>/',views.Crud_delete,name='Crud_delete'),
    path('list/', views.Crud_list,name='Crud_list'),
    #path('search/', views.search,name='search')
    path('crud/search/',views.search,name='search')

]
