from .models import Cart
def count_products(request):
  
    if request.user.is_authenticated:
        user = request.user
        count_products = Cart.objects.filter(user=user).count()
    else:
        count_products = 0

    return {'count_products': count_products}
