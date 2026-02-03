from django.contrib import admin
from .models import Profile, User

# Simple admin registration
admin.site.register(User)
admin.site.register(Profile)
