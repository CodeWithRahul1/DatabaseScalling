from django.urls import path
from app.views import SaleOrderCreateView

urlpatterns = [
    path('api/order/create/', SaleOrderCreateView.as_view(), name='create_order'),
]
