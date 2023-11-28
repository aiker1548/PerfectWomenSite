from datetime import datetime

from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    slug = serializers.SlugField(max_length=255)

    class Meta:
        model = Category
        fields = ('name', 'slug')

class WomenSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(default='photos/2023/11/10/IMG_20190307_114524.jpg')
    time_сreate = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)

    class Meta:
        model = Women
        fields = ("__all__")



# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     slug = serializers.SlugField(max_length=255)
#     content = serializers.CharField(max_length=255)
#     photo = serializers.ImageField(default='photos/2023/11/10/IMG_20190307_114524.jpg')
#     time_сreate = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#
#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data['title']
#         instance.slug = validated_data['slug']
#         instance.content = validated_data['content']
#         instance.photo = validated_data['photo']
#         instance.cat_id = validated_data['cat_id']
#         instance.time_update = datetime.now()
#         instance.save()
#         return instance


# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()

