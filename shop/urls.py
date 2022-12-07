from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('product/<slug:url>/', views.product, name='product'),
    path('search/', views.search, name='search'),
    path('<slug:url>/', views.category, name='category'),
]