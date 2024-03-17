from core.models import Product, ProductImages, Category, CartOrder, CartOrderProducts, ProductReview, WishList
from django.contrib import messages


def default(request):
    categories = Category.objects.all()
    
    try:
        wishlist = WishList.objects.filter(user=request.user)
    except:
        wishlist = 0
        
    
    return{
        'categories': categories,
        'wishlist': wishlist,
    }