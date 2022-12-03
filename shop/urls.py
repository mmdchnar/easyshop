from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('product/<slug:url>/', views.product, name='product'),
    path('<slug:url>/', views.category, name='category'),
]