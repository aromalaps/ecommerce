from . import views
from django.urls import path

app_name='phones'
urlpatterns = [
    
    path('',views.Home,name='Home'),
    path('details/<int:id>',views.Detail,name='detail'),
    path('<slug:c_slug>/',views.Home,name='product_by_category'),
   
]