from django.shortcuts import render, redirect
from .models import Product
from rest_framework.decorators  import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from django.contrib.auth.decorators import user_passes_test
from .forms import ProductForm, GuestForm

# Create your views here.
def index(request):
	#TODO implement pagination
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'dashboard/index.html', context)

#Cart Page View
def cart(request):
	guest_form = GuestForm(request.POST or None)
	if request.method == 'POST':
		if guest_form.is_valid():
			guest_form.save()
			return redirect('index')
	context = {'form':guest_form}
	return render(request, 'dashboard/cart.html', context)

#TODO
def checkout_page(request):
	context = {}
	return render(request, 'dashboard/checkout.html', context)

#Product Form View
@user_passes_test(lambda u: u.is_superuser,  login_url='/admin')
def create_product(request):
	product_form = ProductForm(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if product_form.is_valid():
			product_form.save()
			return redirect('checkout')
	context = {'form':product_form}
	return render(request, 'dashboard/create_product.html', context)

#Api to get products from carts
@api_view(['GET'])
def cart_products(request):
	ids = request.GET.getlist('ids[]')
	products = Product.objects.filter(pk__in = ids)
	serializer = ProductSerializer(products, many=True)
	return Response(serializer.data)