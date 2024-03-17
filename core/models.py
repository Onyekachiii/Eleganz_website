from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User


STATUS = (
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("in_review", "In Review"),
    ("published", "Published"),
)

STATUS_CHOICE = (
    ("processing", "Processing"),
    ("shipped", "Shipped"),
    ("delivered", "Delivered"),
)

RATING = (
    (1, "★✩✩✩✩"),
    (2, "★★✩✩✩"),
    (3, "★★★✩✩"),
    (4, "★★★★✩"),
    (5, "★★★★★"),
)

PRODUCT_TYPES = (
    ('fabric', 'Fabric'),
    ('accessory', 'Accessory'),
)


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='cat_', alphabet="abcdefgh12345678")
    title = models.CharField(max_length=100, default="Category Title")
    image = models.ImageField(upload_to='category', blank=True, null=True, default="category.jpg")
    
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__ (self):
        return self.title
    

class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='prd_', alphabet="abcdefgh12345678")
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")
    
    title = models.CharField(max_length=100, default="Product Title")
    image = models.ImageField(upload_to='product', blank=True, null=True, default="product.jpg")
    description = models.TextField(null=True, blank=True, default="This is the product")
    
    product_type = models.CharField(choices=PRODUCT_TYPES, max_length=20, default='fabric')
    
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1.99, null=True, blank=True)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default=2.99, null=True, blank=True)

    
    product_status = models.CharField(choices=STATUS, max_length=20, default="in_review")
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    
    sku = ShortUUIDField(unique=True, length=10, max_length=20, prefix='sku_', alphabet="abc12345678")
    
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)
    
    
    
    class Meta:
        verbose_name_plural = 'Products'
        
    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__ (self):
        return self.title
    
    def get_percentage(self):
        new_price = (self.old_price - self.price) / self.old_price * 100
        return new_price
    
class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name="product_images", on_delete=models.SET_NULL, null=True)
    images = models.ImageField(upload_to = "product-images", default="product.png")
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Product Images"
        
        


class CartOrder(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1.99, null=True, blank=True)
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="processing")
    
    class Meta:
        verbose_name_plural = "Cart Order"
        

class CartOrderProducts(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200, default=0)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1.99, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=1.99, null=True, blank=True)
    
    
    class Meta:
        verbose_name_plural = "Cart Order Items"
    
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' %(self.image.url))
    
    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' %(self.image))
    

class CartOrderRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    delivery_address = models.TextField()
    delivery_floor_level = models.CharField(max_length=50)
    description = models.TextField(default=None, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} - {self.timestamp}"
    

class ProductReview(models.Model):
    user = models.ForeignKey( User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="reviews")
    rating = models.IntegerField(choices=RATING, default=None)
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Product Reviews"
        
    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating
    
    
class WishList(models.Model):
    user = models.ForeignKey( User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "WishLists"
    
    def __str__(self):
        return self.product.title

    
class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery_images')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title