from django.contrib import admin
from .models import user_profile, Post, categorys, likes,comment,report
# Register your models here.

admin.site.register(user_profile)
admin.site.register(categorys)
admin.site.register(Post)
admin.site.register(likes)
