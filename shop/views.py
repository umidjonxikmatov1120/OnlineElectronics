from django.shortcuts import render, get_object_or_404, redirect

from shop.models import DetailModel, CategoryModel, ProductsModel


def home_page_view(request):
    details = DetailModel.objects.all()
    categories = CategoryModel.objects.all()
    products = ProductsModel.objects.all()
    cat = request.GET.get('cat')

    context = {
        "details": details,
        "categories": categories,
        "products": products,

    }
    return render(request, 'index.html', context=context)


def product_page_view(request, pk):
    product_detail = get_object_or_404(ProductsModel, pk=pk)
    related_products = ProductsModel.objects.all()[:4]
    context = {
        "product_detail": product_detail,
        "related_products": related_products
    }
    return render(request, 'product.html', context=context)


def login_view(request):

    return render(request, 'login.html')


def store_view(request):
    products = ProductsModel.objects.all()
    context = {
        "store_products": products,
    }
    return render(request, 'store.html', context=context)


def add_to_cart(request, pk):
    user_cart = request.session.get('user_cart', [])
    if pk in user_cart:
        user_cart.remove(pk)
    else:
        user_cart.append(pk)
    request.session['user_cart'] = user_cart
    return redirect(request.GET.get('next', '/'))

def show_cart(request):
    user_cart = request.session.get('user_cart', [])
    products = ProductsModel.objects.filter(id__in=user_cart)
    context = {
        "show_products": products
    }
    return render(request, template_name='base.html', context=context)

def add_to_wishlist(request, pk):
    wishlist = request.session.get('user_cart', [])
    if pk in wishlist:
        wishlist.remove(pk)
    else:
        wishlist.append(pk)
    request.session['user_cart'] = wishlist
    return redirect(request.GET.get('next', '/'))


def show_wishlist(request):
    user_wishlist = request.session.get('user_cart', [])
    wishlists = ProductsModel.objects.filter(id__in=user_wishlist)
    context = {
        "show_wishlists": wishlists
    }
    return render(request, template_name='base.html', context=context)