from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Review
from .serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer


@api_view(['GET'])
def products_list_view(request):
    """реализуйте получение всех товаров из БД
    реализуйте сериализацию полученных данных
    отдайте отсериализованные данные в Response"""
    products = Product.objects.all()
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)

class ProductDetailsView(APIView):
    def get(self, request, product_id):
        """реализуйте получение товара по id, если его нет, то выдайте 404
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        products = Product.objects.all()
        for product in products:
            if product.id == product_id:
                serializer = ProductDetailsSerializer(product)
                return Response(serializer.data)
        return Response(status=404)


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        mark = request.query_params.get('mark')
        if mark:
            try:
                mark = int(mark)
                reviews = Review.objects.filter(product_id=product_id, mark=mark)
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)
            except ValueError:
                return Response(status=400)
