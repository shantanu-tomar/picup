from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ('image', 'name')

    def get_name(self, obj):
        return obj.get_image_name()