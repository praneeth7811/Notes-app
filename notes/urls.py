from django.urls import path
from . import views

urlpatterns = [
    path('',views.getdata, name='getdata'),
    path('notes/',views.getnotes, name='getnotes'),
    path('notes/<str:pk>/',views.getNote, name='getnote')
]


