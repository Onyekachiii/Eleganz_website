from django.contrib import admin
from core.models import CartOrder, CartOrderProducts, CartOrderRequest, Product, ProductImages, WishList, GalleryImage
from django import forms
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import path, reverse
from django.utils.html import format_html, mark_safe
from decimal import Decimal


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user', 'title', 'product_image', 'product_type', 'price', 'featured', 'product_status', 'pid']
    
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['title', 'category_image']
    
    
class CartOrderProductsInline(admin.TabularInline):
    model = CartOrderProducts
    extra = 0
    list_display = ['cart_invoice_no', 'item', 'image', 'qty', 'price', 'total']
    

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'paid_status', 'order_date']
    inlines = [CartOrderProductsInline]
    
    
class CartOrderRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'phone', 'delivery_address', 'description', 'paymentEvidence']


class WishListAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']
    
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    



admin.site.register(Product, ProductAdmin)
# admin.site.register(Category, CategoryAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)

admin.site.register(CartOrderRequest, CartOrderRequestAdmin)

admin.site.register(WishList, WishListAdmin)

    