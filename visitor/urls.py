from django.contrib import admin
from django.urls import path
from . import views
app_name='visitor'
urlpatterns = [
    
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('update/<id>/',views.update,name='update'),
    path('list/',views.list_view,name='list'),
    path('checkedin_list/',views.checkedin_list,name='checkedin_list'),
    path('check_out/<pk>/',views.check_out,name='check_out'),
    path('re_entry/<id>/',views.re_entry,name='re_entry'),
    path('detail/<pk>/',views.detail,name='detail'),
    path('print/<pk>/', views.GeneratePdf.as_view(),name='print'),
]
