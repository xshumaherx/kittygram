# Обновлённый views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Cat
from .serializers import CatSerializer


class APICat(APIView):
    def get(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class APICatDetail(APIView):
    def get(self, request, pk):
        cat = Cat.objects.get(id=pk)
        serializer = CatSerializer(cat)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        cat = Cat.objects.get(pk)
        serializer = CatSerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk):
        cat = Cat.objects.get(id=pk)
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        cat = Cat.objects.get(id=pk)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
