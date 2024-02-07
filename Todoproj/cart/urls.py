from . import views
from django.urls import path

app_name='cart_page'
urlpatterns = [
    
    path('add_cart/<int:id>',views.addcart,name='addcart'),
    path('dis_cart/',views.displaycart,name='displaycart'),
 
   
]