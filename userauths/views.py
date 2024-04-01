from django.shortcuts import render, redirect
from userauths.forms import ProfileForm, UserRegisterForm, ContactFormForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from userauths.models import User, Profile
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hey {username}, your account was created successfully!")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect("core:index")
            
    else:
        form = UserRegisterForm()
    
    context = {
        'form': form
    }
    return render(request, "userauths/sign-up.html", context)


# To login users
def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"You are already logged in")
        return redirect("core:index")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
       
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {user.username}!")   
            return redirect("core:index")
            
        else:
            messages.warning(request, f"User with {email} does not exist, Create an account")        
    
    return render(request, "userauths/sign-in.html")


# To logout users
def logout_view(request):
    logout(request)
    messages.success(request, "You logged out successfully!")
    return redirect("userauths:sign-in")


def contact_us(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()

            
            messages.success(request, f"Thank you for contacting us, we will get back to you shortly!")   
            return redirect("core:index")
    else:
        form = ContactFormForm()

    return render(request, 'userauths/contact-us.html', {'form': form})

@login_required
def edit_profile(request):
    profile = request.user.profile
    
    if request.method == "POST":
        profile.first_name = request.POST.get('first_name')
        profile.last_name = request.POST.get('last_name')
        profile.bio = request.POST.get('bio')
        profile.phone = request.POST.get('phone')
        profile.house_address = request.POST.get('house_address')
        profile.city = request.POST.get('city')
        profile.country = request.POST.get('country')
        if 'image' in request.FILES:
            profile.image = request.FILES['image']
        profile.save()
        return redirect('core:dashboard')  # Redirect to dashboard after saving
        
    context = {
        'profile': profile
    }
    return render(request, 'core/dashboard.html', context)

