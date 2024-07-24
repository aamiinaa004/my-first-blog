
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('amina', views.amina, name='HOME'),
    
    
    

    path('home', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('calcul', views.calcul, name='calcul'),



    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]
