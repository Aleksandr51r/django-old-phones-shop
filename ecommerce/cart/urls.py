from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name="cart"),
    path('add_cartitem/<int:product_id>',
         views.add_cartitem, name="add_cartitem"),
    path('remove_cartitem/<int:cartitem_id>',
         views.remove_cartitem, name="remove_cartitem"),

]
