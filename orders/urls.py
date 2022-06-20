from django.urls import path
from . import views
urlpatterns = [
    path('',views.OrdersViews.as_view(), name="orders"),
    path('<int:order_id>/',views.ManageOrderViews.as_view(),name="manage order"),
    path('order/<int:customer_id>/',views.CustumerOrdesViews.as_view(),name="customer orders")

]