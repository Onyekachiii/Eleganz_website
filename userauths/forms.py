from django import forms 
from django.contrib.auth.forms import UserCreationForm
from userauths.models import ContactUs, User, Profile


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Lastname'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    house_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    phone = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Phone Number'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City'}))
    
    class Meta:
        model = User
        fields = ['username', 'email']
    

class ContactFormForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Full name"})) 
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Phone"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Address"}))
    information = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'message'}))
    
    
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'phone', 'address', 'information']
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'phone', 'house_address', 'city', 'country', 'image']