from django.urls import path
from . import views
urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:catagory_slug>/', views.store, name='specific_product'),
    path('<slug:catagory_slug>/<slug:product_slug>', views.product_detail, name='product_detail')
]
