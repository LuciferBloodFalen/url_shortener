from rest_framework import serializers
from .models import UrlMapping
from django.conf import settings


class UrlMappingSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UrlMapping
        fields = [
            'original_url',
            'short_code',
            'short_url',
            'created_at',
        ]
        read_only_fields = ["short_code", "created_at"]

    def validate_original_url(self, value):
        serializer = serializers.URLField()
        serializer.run_validation()
        return value
    
    def get_short_url(self, obj):
        request = self.context.get("request")

        if request:
            base_url = request.build_absolute_uri("/")[:-1]
        else:
            base_url = settings.BASE_URL
        
        return f"{base_url}/{obj.short_code}"