from rest_framework import serializers

from main.models import Product, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewListingField(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

class ProductListSerializer(serializers.ModelSerializer):
    # реализуйте поля title и price
    class Meta:
        model = Product
        fields = ['title', 'price']


class ProductDetailsSerializer(serializers.ModelSerializer):
    # реализуйте поля title, description, price и reviews (список отзывов к товару)
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'reviews']
