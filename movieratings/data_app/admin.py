from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User as Rater

from .models import Movie, Rating, User
# Register your models here.


admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(User)

"""class UserInline(admin.StackedInline):
    model = User
    can_delete = False
    verbose_name_plural = 'user'


class UserAdmin(UserAdmin):
    inlines = (UserInline, )

admin.site.unregister(Rater)
admin.site.register(Rater, UserAdmin)"""
