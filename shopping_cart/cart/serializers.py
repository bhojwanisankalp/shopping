from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
	image_url = serializers.SerializerMethodField('get_image_url')

	class Meta:
		model = Product
		fields  = ['id','name','product_type','price','image_url','description']

	def get_image_url(self, product):
		image_url = product.image.url
		return image_url