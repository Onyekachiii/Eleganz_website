from django.urls import path
from core.views import about_us, add_to_cart, add_to_wishlist, cart_view, checkout_view, delete_item_from_cart, filter_product, get_product_data, index, order_completed_view, product_detail_view, product_list_view, remove_from_wishlist, search_view, update_cart, user_dashboard, user_history, wishlist_view, gallery


app_name = "core"

urlpatterns = [
    path('', index, name='index'),
    
    # # For Categories
    # path('category/', category_list_view, name='category-list'),
    # path('category/<cid>/', category_product_list_view, name='category-product-list'),
    
    # For products
    path('products/', product_list_view, name='product-list'),
    path('products/<str:product_type>/<pid>/', product_detail_view, name='product-detail'),
    path('get-product-data/', get_product_data, name='get_product_data'),
    
    # About us
    path('about-us/', about_us, name='about-us'),
    
    # Search
    path('search/', search_view, name='search'),
    
    # Filter product URL
    path('filter-products/', filter_product, name='filter-product'),
    
    # Wishlist page URL
    path('wishlist/', wishlist_view, name='wishlist'),
    
    # Adding to wishlist
    path('add-to-wishlist/', add_to_wishlist, name='add-to-wishlist'),
    
    # Deleting from wishlist
    path('remove-from-wishlist/', remove_from_wishlist, name='remove-from-wishlist'),
    
    
    #Add to cart URL
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    
    # checkout url
    path('checkout/', checkout_view, name='checkout'),
    
    # Order Completed
    path('checkout/core/order-completed/', order_completed_view, name='order-completed'),
    
    # Cart page URL
    path('cart/', cart_view, name='cart'),
    
    # Delete item from cart
    path('delete-from-cart/', delete_item_from_cart, name='delete-from-cart'),
    
    # Update items in cart
    path('update-cart/', update_cart, name='update-cart'),
    
    # checkout url
    path('checkout/', checkout_view, name='checkout'),
    
    # Customer Dashboard
    path('dashboard/', user_dashboard, name='dashboard'),
    
    # User History
    path('user-history/', user_history, name='user-history'),
    
    # Gallery
    path('gallery/', gallery, name='gallery'),
    
]