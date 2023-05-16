from django.conf import settings
from django.contrib import admin
from django.contrib.auth import get_user_model

client = get_user_model()
admin.site.register(client)
