from rest_framework import serializers
from .models import blog

class blogSerialziers(serializers.ModelSerializer):
    class Meta:
        model=blog
        fields='__all__'