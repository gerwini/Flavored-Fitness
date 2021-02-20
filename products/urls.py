from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='store'),
    path('purchase', views.view_purchase, name='view_purchase'),
    path('<int:product_id>', views.product_info, name='product_info'),
    path('add/<item_id>', views.add_for_purchase, name='add_for_purchase'),
    path('modify/<item_id>', views.modify_purchase, name='modify_purchase'),
    path('remove/<item_id>', views.remove_product, name='remove_product'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
