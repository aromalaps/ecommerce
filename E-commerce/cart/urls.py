from . import views
from django.urls import path

app_name='cart_page'
urlpatterns = [
    
    path('add_cart/<int:id>',views.addcart,name='addcart'),
    path('dis_cart/',views.displaycart,name='displaycart'),
    path('remove_cart/<int:id>',views.removecart,name='removecart'),

    path('fullremove/<int:id>',views.fullremove,name='fullremove'),
    # remove all products in the cart
    path('Place_order/', views.place_order, name='place_order'), 
    path('remove/', views.removeall, name='clear_cart'), 
    path('orderplaced/',views.order_placed,name='order_placed')

 
]