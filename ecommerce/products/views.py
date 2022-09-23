
import random
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Product, Categories

# Create your views here.
def home(request):
    products = Product.objects.all()
    categories = Categories.objects.all()
    items = list(products)
    hero_product = random.choice(items)
    if "carts" in request.session:
        print(request.session["carts"])
    return render(request, "products/index.html" , context = {"products" : products, "hero_product" : hero_product, "categories":categories})
    


def category(request, name):
    category = Categories.objects.get(name=name)
    products = Product.objects.filter(category=category)
    return render(request, "products/index.html" , context = {"products" : products})


def add_to_cart(request, id):
    request.session.modified = True
    
    product = get_object_or_404(Product, id=id) 

    if not product:
        return HttpResponse("there is not product with that id")
    product = {
        "id":product.id,
        "title":product.title,
        "desc":product.desc,
        "price":product.price,
        "category":product.category.name,
        "image":product.image.url
    }
    if "carts" in request.session:
        if not any(int(p['id']) == int(product["id"]) for p in request.session["carts"]):
            request.session["carts"].insert(0, product)
        else:
            return HttpResponse("item is already in the cart")
    else:
        request.session["carts"] = [product]
    return HttpResponse("product added to cart")


def get_carts(request):
    carts = None;
    if "carts" in request.session:
        carts = request.session["carts"]
    carts={"carts":carts}
    return JsonResponse(carts)