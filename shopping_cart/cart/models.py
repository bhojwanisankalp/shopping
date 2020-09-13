from django.db import models




class Product(models.Model):
	"""Model For Product"""
	name = models.CharField(max_length=200, default='', null=False)
	product_type = models.CharField(max_length=200, default='', null=False)
	price = models.FloatField(null = True)
	description = models.CharField(max_length=500, null=True)
	image = models.ImageField(upload_to='products/')
	currency_type = models.CharField(max_length=200, default='INR', null=False)
	created_at  = models.DateTimeField(auto_now_add = True, null = True)
	updated_at = models.DateTimeField(auto_now = True, null = True)

	def __str__(self):
		""" String representation of Model Instance """
		return self.name


class Cart(models.Model):
	"""Model For Cart"""
	created_at  = models.DateTimeField(auto_now_add = True, null = True)
	updated_at = models.DateTimeField(auto_now = True, null = True)
	

class Guest(models.Model):
	"""Model For Guest"""
	name = models.CharField(max_length=200, null=True)
	email = models.EmailField(max_length=200, null=True)
	address_one = models.CharField(max_length=200, null=True)
	address_two = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	state = models.CharField(max_length=200, null=True)
	pin = models.IntegerField(null=True)
	created_at  = models.DateTimeField(auto_now_add = True, null = True)
	updated_at = models.DateTimeField(auto_now = True, null = True)
	
class Cart_Product(models.Model):
	"""Mapping for Cart and Product"""
	cart = models.ForeignKey(Cart, on_delete = models.CASCADE, null = False)
	product = models.ForeignKey(Product, on_delete = models.CASCADE, null = False)
				