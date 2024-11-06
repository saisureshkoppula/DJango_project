from django.urls import path 
from . import views 

urlpatterns = [
    path('first/',views.firstview),
    path('hi/',views.secondview)

]
