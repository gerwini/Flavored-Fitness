from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='store'),
    path('purchase', views.view_purchase, name='view_purchase'),
    path('<product_id>', views.product_info, name='product_info'),
    path('add/<item_id>', views.add_for_purchase, name='add_for_purchase'),
]
