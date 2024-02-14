from .models import Category
from cart.models import Cart

def menu_links(req):
    links=Category.objects.all()
    return dict(links=links)

