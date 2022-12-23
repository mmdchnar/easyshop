from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('login/', views.login, name='login'),
    path('cart/', views.cart, name='cart'),
    path('product/<str:url>/', views.product, name='product'),
    path('<slug:url>/', views.categories_and_brands, name='category'),
]
