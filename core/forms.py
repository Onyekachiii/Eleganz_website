from django import forms
from core.models import CartOrderRequest, ProductReview


class ProductReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'Placeholder': "Write review"}))
    
    class Meta:
        model = ProductReview
        fields = ['review', 'rating']


class CartOrderRequestForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Phone"}))
    delivery_address = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Delivery Address"}))
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "Description"}))
    
    
    class Meta:
        model = CartOrderRequest
        fields = ['first_name', 'last_name', 'email', 'phone', 'delivery_address', 'description']