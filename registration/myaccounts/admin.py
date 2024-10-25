from django.contrib import admin
from .models import UserRegistration,Post
from myaccounts.models import Post

admin.site.register(UserRegistration)
admin.site.register(Post)
