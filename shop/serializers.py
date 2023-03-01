from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'image', 'price', 'discount', 'rating')


class ProductDetailSerializer(serializers.ModelSerializer):
    material = MaterialSerializer(read_only=True, many=True)
    product_comment = CommentSerializer(read_only=True, many=True)
    product_rating = RatingSerializer(read_only=True, many=True)
    product_image = ProductImageSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'description', 'image', 'price', 'discount', 'rating',
                  'material', 'product_comment', 'product_rating', 'product_image')
