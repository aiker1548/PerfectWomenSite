from rest_framework import generics
from .models import *
from django.shortcuts import render
from .serializers import WomenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
class WomenAPIView(APIView):
    def get(self, request):
        return Response({'GoodMan': 1})

    def post(self, request):
        name = request.query_params.get('name', None)
        slug = request.query_params.get('slug', None)
        # Проверяем наличие ключей 'name' и 'slug' в request.data
        if name and slug:
            new_post = Category.objects.create(
                name=name,
                slug=slug
            )
            return Response({'post': model_to_dict(new_post)})
        else:
            # Возвращаем сообщение об ошибке, если ключи отсутствуют
            return Response({'error': 'Missing required keys "name" and "slug"'}, status=400)

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer