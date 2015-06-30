from django.contrib import admin
from .models import Movies, Ratings, User
# Register your models here.
admin.site.register(Movies)
admin.site.register(Ratings)
admin.site.register(User)
