from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name = 'homepage'),
    path('contact/', views.contact, name= "contacts"),

    #ex:detail page
    path('<int:pk>/', views.detailPage, name= "detail"),

]