from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(user_profile)
admin.site.register(categorys)
admin.site.register(Post)
admin.site.register(comment)
