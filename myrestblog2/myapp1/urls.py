from django.contrib import admin
from django.urls import path,include
from myapp1 import views

urlpatterns = [
    path('getalldata/',views.getalldata),
    path('getid/<int:id>/',views.getid),    
    path('saveuser/',views.saveuser),
    path('deleteuser/<int:id>/',views.deleteuser),
    path('updateuser/<int:id>/',views.updateuser),
]
    
   