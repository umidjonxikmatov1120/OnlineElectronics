from django.urls import path

from shop.views import home_page_view, product_page_view, login_view, store_view, add_to_cart, show_cart, \
    add_to_wishlist, show_wishlist

urlpatterns = [
    path('', home_page_view, name='home'),
    path('products/<int:pk>/', product_page_view, name='product_page'),
    path('login/', login_view, name='login'),
    path('store/', store_view, name='store'),
    path('add-cart/<int:pk>/', add_to_cart, name='add-or-remove-cart'),
    path('cart/', show_cart, name='show-cart'),
    path('add-wishlist/<int:pk>/', add_to_wishlist, name='add-or-remove-wishlist'),
    path('wishlist/', show_wishlist, name='show-wishlist'),
]
