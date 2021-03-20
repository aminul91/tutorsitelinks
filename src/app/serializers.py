from rest_framework import serializers
from app.models import *
# Register your models here.

class linksSerializer(serializers.ModelSerializer):
    class Meta:
        model = tutorials_path
        fields = '__all__'
