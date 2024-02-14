from django.shortcuts import render,redirect
from Todoapp.models import Product
from .models import Cart
from django.core.exceptions import ObjectDoesNotExist


#add items to the cart and add quantity of the product
def addcart(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    print(product)
    print(user)
    try:
        cart=Cart.objects.get(product=product,user=user)
        if cart.quantity<cart.product.stock:
            cart.quantity+=1
            cart.save()
    except Cart.DoesNotExist:
        cart=Cart.objects.create(user=user,product=product,quantity=1)

    return redirect('cart_page:displaycart')


def displaycart(req):
    cart = Cart.objects.filter(user=req.session['user'])  # Retrieve cart items
    grand_total = sum(item.quantity * item.product.price for item in cart)  # Calculate grand total
    return render(req, 'cart.html', {'cart': cart, 'grand_total': grand_total})


def order_placed(req):
    return render(req,'order_placed.html')




#remove the quantity of the product in cart using cart button (-) .
def removecart(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    cart=Cart.objects.get(product=product,user=user)
    if cart.quantity>1:
        cart.quantity-=1
        cart.save()
    return redirect('cart_page:displaycart')


# remove single product from the cart
def fullremove(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    cart=Cart.objects.get(product=product,user=user)
    cart.delete()
    return redirect('cart_page:displaycart')
#place order is decrement the quantity of the product in the data base and clear the cart
def place_order(req):
    user = req.session['user']
    cart_items = Cart.objects.filter( user=user )
   
    for cart_item in cart_items:
        products=Product.objects.get(id=cart_item.product.id)
        #stock update after purchasing substrating the quantity
        products.stock-=cart_item.quantity
        products.save()
        #delete the whole products in the cart
        cart_item.delete()
    return redirect('phones:Home')

#remove the whole products in the cart

def removeall(req):
    user = req.session['user']
    cart_items = Cart.objects.filter( user=user)
    for i in cart_items:
        i.delete()
    return redirect('phones:Home')
