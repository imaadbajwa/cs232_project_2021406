from django.contrib import admin
from .models import UserProfile
from .models import UserDetail
from django.contrib.auth.models import User
from .models import UserProfile, UserDetail



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_email', 'get_first_name', 'get_last_name', 'phone_number']

    def get_email(self, obj):
        return obj.user.email

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    get_email.short_description = 'Email'
    get_first_name.short_description = 'First Name'
    get_last_name.short_description = 'Last Name'

admin.site.register(UserProfile, UserProfileAdmin)
class UserDetailInline(admin.StackedInline):
    model = UserDetail
    can_delete = False
class UserAdmin(admin.ModelAdmin):
    inlines = (UserDetailInline,)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

