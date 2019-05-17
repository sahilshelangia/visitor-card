from django.urls import path
from . import views
import visitor.views

urlpatterns = [
    path('signup/',views.SignupView.as_view(),name='signup' ),

    path('profile/',visitor.views.index,name='index' ),

]