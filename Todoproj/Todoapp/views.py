from django.shortcuts import render,get_object_or_404
from .models import Product,Category
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def Home(req,c_slug=None,stock=None):
    c_page=None
    product_list=None
    if c_slug !=None :
        c_page=get_object_or_404(Category,slug=c_slug)
        product_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        product_list=Product.objects.all().filter(available=True)



    paginator=Paginator(product_list,4)

    try: 
        page=int(req.GET.get('page', '1')) 
    except:
        page=1  
    # invalid page and empty page
    try: 
        products=paginator.page(page) 
    except( EmptyPage, InvalidPage): 
        products=paginator.page(paginator.num_pages)
    return render(req,"index.html",{'phones':product_list,'category':c_page,'products': products})


def Detail(req,id):
    detail=Product.objects.get(id=id)
    return render(req,"details.html",{'details':detail,})
