
from rest_framework import serializers
from .models import Product
from categories.models import Category
from categories.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_details = CategorySerializer(source='category', read_only=True)
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "description",
            "stock_quantity",
            "img_url",
            "created_at",
            "updated_at",
            "category",
            "category_details"
        ]

class ListProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "description",
            "stock_quantity",
            "img_url",
            "created_at",
            "updated_at",
            "category",
        ]


# category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
#     name = models.CharField(max_length=150)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     stock_quantity = models.IntegerField()
#     img_url = models.ImageField(upload_to="products/")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
