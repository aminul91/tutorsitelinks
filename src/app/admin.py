from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(user_info)
admin.site.register(tutorial_type)
admin.site.register(language_type)
admin.site.register(links_db)
admin.site.register(suggestion)
