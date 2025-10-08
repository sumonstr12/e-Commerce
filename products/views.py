from django.shortcuts import render
from .serializers import ProductSerializer, ListProductSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Product
# Create your views here.


class CreateProductView(APIView):
    def post(self, request):
        print(request.data.get("category"))
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success" : True,
                    "message" : "Product created Successfully"
                },status=status.HTTP_201_CREATED
            )

        return Response(
            {
                "success": False,
                "message" : "Failed to Create Product"
            },status=status.HTTP_400_BAD_REQUEST
        )
    


class UpdateProductView(APIView):
    def put(self, request, id):
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "success" : True,
                        "message" : "Updated Sucessfull"
                    }, status=status.HTTP_200_OK
                )
            return Response({
                "success" : False,
                "message" : "Error"
            }, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({
                "success" : False,
                "message" : "Error"
            }, status=status.HTTP_400_BAD_REQUEST)
        


class DeleteProductView(APIView):
    def delete(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
            product.delete()
            return Response(
                {
                    "success" : True,
                    "message" : "Successful to delete"
                }, status=status.HTTP_200_OK
            )
        except Product.DoesNotExist:
            return Response(
                {
                    "success" : False,
                    "message" : "Failed to delete"
                }, status=status.HTTP_400_BAD_REQUEST
            )
    
class ProductByIdView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
            serializer = ProductSerializer(product)
            return Response(
                {
                    "success" : True,
                    "message" : "Product View Ready.",
                    "data" : serializer.data
                }, status=status.HTTP_200_OK
            )
        except Product.DoesNotExist:
            return Response(
                {
                    "success" : False,
                    "message" : "Product doesnot exists"
                }, status=status.HTTP_404_NOT_FOUND
            )
        

class ListProductView(APIView):
    def get(self, request):
        list_product = Product.objects.all()
        serializer = ListProductSerializer(list_product, many=True)
        return Response(
            {
                "success" : True,
                "message" : " List View Ready",
                "data" : serializer.data
            }, status=status.HTTP_200_OK
        )