from rest_framework import serializers
from .models import trapImage

class trapImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = trapImage
        fields= "__all__"