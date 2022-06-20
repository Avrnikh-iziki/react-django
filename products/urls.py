from django.urls import path
from . import views

urlpatterns = [
    path('<int:number_pag>/',views.AllProducts.as_view(), name='products'),
    path('addproduct/',views.AddProduct.as_view(), name='add_product'),
    path('edit/<int:product_id>/',views.ProductsManagment.as_view(),name='edit_products'),
]
