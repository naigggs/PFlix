from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.getRoutes, name="routes"),
    path('api/products', views.getProducts, name="products"),
    path('api/products/create', views.addProduct, name="addproducts"),
    path('api/products/<str:pk>', views.getProduct, name="product"),
    path('api/directors', views.getDirectors, name="directors"),
    path('api/directors/<str:pk>', views.getDirector, name="directors"),
    path('api/directorproducts/<str:pk>', views.getDirectorProducts, name="directorproducts"),
]