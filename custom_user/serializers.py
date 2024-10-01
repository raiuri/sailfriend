from rest_framework import serializers
from .models import InterestCategory, Interest

class InterestCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestCategory
        fields = ['id', 'name']

