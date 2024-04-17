from __future__ import print_function
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from userauths.models import Profile
from core.models import CartOrder, CartOrderProducts, Product, ProductImages, ProductReview, WishList, GalleryImage
from core.forms import ProductReviewForm, CartOrderRequestForm
from django.core import serializers
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index (request):
    fabrics = Product.objects.filter(product_type='fabric')
    accessories = Product.objects.filter(product_type='accessory')
    products = Product.objects.filter(product_status='published', featured=True)
    # categories = Category.objects.all()
    images = GalleryImage.objects.all()
    
    context = {
        "fabrics": fabrics,
        "accessories": accessories,
        # "categories": categories,
        "images": images,
        "products": products,
    }
    return render(request, 'core/index.html', context)


# For about us page
def about_us(request):
    return render(request, 'core/about_us.html')


# To list products in shop
def product_list_view(request):
    fabrics = Product.objects.filter(product_type='fabric')
    accessories = Product.objects.filter(product_type='accessory')
    products = Product.objects.filter(product_status='published', featured=True)
   
    
    context = {
        "fabrics": fabrics,
        "accessories": accessories,
        "products": products,

    }
    return render(request, 'core/product-list.html', context)
    


# To get a product detail
def product_detail_view(request, product_type, pid):
    if product_type == 'fabric':
        product = get_object_or_404(Product, pid=pid, product_type='fabric')
    elif product_type == 'accessory':
        product = get_object_or_404(Product, pid=pid, product_type='accessory')
    else:
        # Handle invalid product type
        return HttpResponseNotFound("Invalid product type")

    # To get all reviews
    reviews = ProductReview.objects.filter(product=product).order_by("-date")

    # Product review form
    review_form = ProductReviewForm()

    make_review = True

    if request.user.is_authenticated:
        user_review_count = ProductReview.objects.filter(user=request.user, product=product).count()

        if user_review_count == 1:
            make_review = False

    product_images = product.product_images.all()

    context = {
        "p": product,
        "make_review": make_review,
        "review_form": review_form,
        "product_images": product_images,
        "reviews": reviews,
        "product": product,
        "product_id": pid,  # Pass product ID to the template
    }
    return render(request, 'core/product-detail.html', context)


# To search for products
def search_view(request):
    query = request.GET.get('q')
    
    if query is not None:
        products = Product.objects.filter(title__icontains=query).order_by('-date')
    
    
        context = {
            "query": query,
            "products": products,
        }
        return render(request, 'core/search.html', context)
    else:
        return render(request, 'core/search.html')   


# To filter products by categories & vendors
def filter_product(request):
    # categories = request.GET.getlist('category[]')
    
    products = Product.objects.filter(product_status= "published").order_by("-id").distinct()
    
        
    data = render_to_string("core/async/product-list.html", {"products": products})
    return JsonResponse({"data":data})


def get_product_data(request):
    products = Product.objects.all()
    data = [{'id': product.id, 'title': product.title, 'image': product.image.url, 'price': product.price, 'old_price': product.old_price} for product in products]
    return JsonResponse(data, safe=False)


# To add to cart
@login_required
def add_to_cart(request):
    cart_product = {}
    cart_product[str(request.GET['id'])] = {
        'title': request.GET['title'],
        'price': request.GET['price'],
        'qty':  request.GET['qty'],
        'image': request.GET['image'],
        'pid': request.GET['pid'],
    }
    
    if 'cart_data_obj' in request.session:
        if str(request.GET['id']) in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = int(cart_product[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cart_data_obj'] = cart_data
            
        else:
            cart_data = request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data
    
    else:
        request.session['cart_data_obj'] = cart_product
        
    return JsonResponse({"data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj'])})


# To list products in cart
def clean_price_string(price_string):
    return ''.join(char for char in price_string if char.isdigit() or char == '.')

@login_required
def cart_view(request):
    cart_total_amount = 0

    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            if item['qty'] and item['price']:
                # Clean the price string before conversion
                cleaned_price_string = clean_price_string(item['price'])

                try:
                    cart_total_amount += int(item['qty']) * float(cleaned_price_string)
                except ValueError:
                    messages.error(request, f"Invalid price format for item {p_id}. Please check your cart.")
                    return redirect('core:index')

        return render(request, 'core/cart.html', {"cart_data": request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount': cart_total_amount})
    else:
        messages.warning(request, "Your cart is empty")
        # Redirect to the login page if the user is not authenticated
        return redirect('userauths:sign-in')
    
    
# To delete item from cart
@login_required
def delete_item_from_cart(request):
    product_id = str(request.GET['id'])
    if 'cart_data_obj' in request.session:
        if product_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            del request.session['cart_data_obj'][product_id]
            request.session['cart_data_obj'] = cart_data
            
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for product_id, item in request.session['cart_data_obj'].items():
            if item['qty'] and item['price']:
                # Clean the price string before conversion
                cleaned_price_string = clean_price_string(item['price'])

                try:
                    cart_total_amount += int(item['qty']) * float(cleaned_price_string)
                except ValueError:
                    messages.error(request, f"Invalid price format for item. Please check your cart.")
                    return redirect('core:index')
    
    context = render_to_string("core/async/cart-list.html", {"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount': cart_total_amount})
    return JsonResponse({"data":context, 'totalcartitems': len(request.session['cart_data_obj'])})


# To update cart
@login_required
def update_cart(request):
    product_id = str(request.GET['id'])
    product_qty = int(request.GET['qty'])
    
    if 'cart_data_obj' in request.session:
        if product_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = product_qty
            request.session['cart_data_obj'] = cart_data
            
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for product_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price']) 
    
    context = render_to_string("core/async/cart-list.html", {"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount': cart_total_amount})
    return JsonResponse({"data":context, 'totalcartitems': len(request.session['cart_data_obj'])})


# To checkout
# To checkout
@login_required
def checkout_view(request):
    cart_total_amount = 0
    total_amount = 0

    # Initializing the form variable
    form = CartOrderRequestForm()

    # Checking if cart_data_obj is in session
    cart_data_obj = request.session.get('cart_data_obj', None)
    
    if cart_data_obj is None:
        cart_data_obj = {} 
        
    if cart_data_obj:
        for product_id, item in cart_data_obj.items():
            total_amount += int(item['qty']) * float(item['price'])

        # Creating order objects
        order = CartOrder.objects.create(
            user=request.user,
            price=total_amount,
        )

        # Getting total amount for the cart
        for product_id, item in cart_data_obj.items():
            cart_total_amount += int(item['qty']) * float(item['price'])

            cart_order_products = CartOrderProducts.objects.create(
                order=order,
                invoice_no="INVOICE_NO-" + str(order.id),
                item=item['title'],
                image=item['image'],
                qty=item['qty'],
                price=item['price'],
                total=float(item['qty']) * float(item['price']),
            )

    if request.method == 'POST':
        form = CartOrderRequestForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.user = request.user
            form.save()

            # Clear the cart_data_obj from the session after processing
            del request.session['cart_data_obj']

            messages.success(request, 'Your cart order request has been submitted successfully.')
            return redirect('core/order-completed')
        else:
            # Print form errors for debugging
            print(form.errors)

    else:
        # Get the user's profile
        user_profile = Profile.objects.get(user=request.user)

        # Prepopulate form fields with user profile data
        form = CartOrderRequestForm(initial={
            'first_name': user_profile.first_name,
            'last_name': user_profile.last_name,
            'email': user_profile.user.email,
            'phone': user_profile.phone,
        })

    return render(request, 'core/checkout.html', {'cart_data_obj': cart_data_obj,
                                                   'totalcartitems': len(cart_data_obj),
                                                   'cart_total_amount': cart_total_amount,
                                                   'form': form})
    

@login_required
def order_completed_view(request):
    
    return render(request, 'core/order-completed.html')


# To add to wishlist
def add_to_wishlist(request):
    id = request.GET['id']
    product = Product.objects.get(id=id)
    
    context = {}
    
    wishlist_count = WishList.objects.filter(user=request.user, product=product).count()
    
    if wishlist_count > 0:
        context = {
            "bool": True,
        }
    else:
        new_wishlist = WishList.objects.create(
            product=product,
            user=request.user
        )
        context ={
            "bool": True,
        }
    
    return JsonResponse(context)



# To view wishlist
@login_required
def wishlist_view(request):
    wishlist = WishList.objects.filter(user=request.user)

    context = {
        "w" : wishlist,
    }
    return render(request, "core/wishlist.html", context)


# To remove from wishlist
@login_required
def remove_from_wishlist(request):
    pid = request.GET.get('id')
    if pid:
        product = get_object_or_404(WishList, id=pid)
        wishlist = WishList.objects.filter(user=request.user)
        product.delete()
    
        context = {
            "bool" : True,
            "w": wishlist,
        }
        wishlist_json = serializers.serialize('json', wishlist)
        data = render_to_string("core/async/wishlist-list.html", context)
        return JsonResponse({"data": data, "w": wishlist_json})
    else:
        return JsonResponse({"error": "Invalid parameters"}, status=400)
    

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'core/gallery.html', {'images': images})

def about_us(request):
    return render(request, 'core/about-us.html')



@login_required
def user_dashboard(request):
    user = request.user
    orders = CartOrder.objects.filter(user=user)
    profile = request.user.profile

    context = {
        'user': user,
        'orders': orders,
        'profile': profile
    }
    return render(request, 'core/dashboard.html', context)

@login_required
def user_history(request):
    orders = CartOrderProducts.objects.filter(order__user=request.user).order_by("-id")
    context = {
        "orders": orders,
    }
    return render(request, 'core/user-history.html', context)
