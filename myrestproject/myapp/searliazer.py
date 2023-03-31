from rest_framework import serializers
from .models import mynotes

class userSerialziers(serializers.ModelSerializer):
    class Meta:
        model=mynotes
        fields='__all__'


