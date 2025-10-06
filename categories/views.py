from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import status

from .models import Category
# Create your views here.


class CreateCategoryView(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "message" : "Category Created Successfully"
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "success" : "Failed",
                "message" : "Failed to Created Category"
            }, status=status.HTTP_400_BAD_REQUEST
        )

class UpdateCategoryView(APIView):
    def put(self, request):
        category_id = request.data.get("id")
        # print(category_id)

        try:
            category = Category.objects.get(id=category_id)
            print(category.name)
        except Category.DoesNotExist:
            return Response(
                {
                    "success" : "false",
                    "message" : "Category not Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success" : "true",
                    "message" : "Updated Sucessfully"
                },status=status.HTTP_200_OK
            )
        return Response(
            {
                "success" : "false",
                "message" : "Failed to Update Category"
            }, status=status.HTTP_400_BAD_REQUEST
        )
    

class DeleteCategoryView(APIView):
    def delete(self, request):
        category_id = request.data.get("id")
        try:
            category = Category.objects.get(id=category_id)
            category.delete()
            return Response(
                {
                    "success" : "True",
                    "message": "Deleted successfully"
                }, status=status.HTTP_200_OK
            )
        except Category.DoesNotExist:
            return Response(
                {
                    "success" : "false",
                    "message" : "Category not Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )



class CategoryByIdView(APIView):
    def post(self, request, id):
        try:
            category = Category.objects.get(id=id)
            serializer = CategorySerializer(category)
            return Response(
                {
                    "success" : "true",
                    "message": "Category by id successful",
                    "data" : serializer.data
                }
            )
        except Category.DoesNotExist:
            return Response(
                {
                    "success" : "false",
                    "message" : "Failed"
                }, status=status.HTTP_400_BAD_REQUEST
            )
    

class ListCategoryView(APIView):
    def get(self, request):
        # list_category = Category.objects.filter()
        list_category = Category.objects.all() # same as using filter
        serializer = CategorySerializer(list_category, many=True)
        return Response(
            {
                "status" : "Success",
                "message" : "List Created SuccessFully",
                "data" : serializer.data
            },
            status=status.HTTP_200_OK
        )
