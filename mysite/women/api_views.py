from rest_framework import generics
from .models import *
from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework import generics, viewsets



class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class WomenAPIView(APIView):
#
#     def get(self, request):
#         try:
#             womens = Women.objects.all()
#         except:
#             return Response({'error': 'Can`t get objects of Women class'})
#
#         return Response(WomenSerializer(womens, many=True).data)
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'new_post': serializer.validated_data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if pk is None:
#             return Response({'error': 'Doesn`t catch pk of object'})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': f'Object with pk={pk} doens`t exists'})
#
#         serializer = WomenSerializer(data=request.query_params, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer