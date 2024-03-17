from django.contrib import admin
from userauths.models import User, Profile, ContactUs

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'phone')
    

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'address')

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
