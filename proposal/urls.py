from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   path('', views.home,name="home"),
   path('topics/', views.topics,name="topics"),
   path('contact/', views.contact,name="contact"),
   path('<str:slug>/', views.detail,name="details"),
   path('search', views.search, name='search'),


]