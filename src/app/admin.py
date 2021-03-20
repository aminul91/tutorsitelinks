from django.contrib import admin
from app.models import *
# Register your models here.

from .models import *
admin.site.register(user_info)
admin.site.register(tutorial_type)
admin.site.register(language_type)
admin.site.register(tutorials_path)
admin.site.register(suggestion)
