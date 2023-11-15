from rest_framework import serializers
from .models import *



class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content

    title = serializers.CharField(max_length=255, verbose_name='Заголовок')
    slug = serializers.SlugField(max_length=255, unique=True, verbose_name='URL', db_index=True)
    content = serializers.TextField(blank=True, verbose_name='Текст статьи')
    photo = serializers.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фото')
    time_сreate = serializers.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = serializers.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = serializers.BooleanField(default=True, verbose_name='Опубликовано')
    cat = serializers.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

