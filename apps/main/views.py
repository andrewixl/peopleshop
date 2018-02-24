from django.shortcuts import render, redirect, HttpResponse
from .models import Apparel, Picture, Colors, Sizes, Contact, Shipping
from django.contrib import messages

# Create your views here.
def genErrors(request, Emessages):
	for message in Emessages:
		messages.error(request, message)

def index(request):
    return render(request, 'main/index.html')

def categories(request, id):
	if id == "apparel":
		products = Apparel.objects.filter().all()
	if id == "men":
		products = Apparel.objects.filter(product_type = "men").all()
	if id == "women":
		products = Apparel.objects.filter(product_type = "women").all()
	if id == "kids":
		products = Apparel.objects.filter(product_type = "kids").all()

	context = {
	"products":products,
	}
	return render(request, 'main/categories.html', context)

def product(request, type_id, product_id):
	if type_id == "men":
		product = Apparel.objects.get(id = product_id)
		photos = Picture.objects.filter(master_apparel_product = product_id).all()
		colors = Colors.objects.filter(master_apparel_product = product_id).all()
		sizes = Sizes.objects.filter(master_apparel_product = product_id).all()
		shipping = Shipping.objects.filter(master_apparel_product = product_id).all()
	if type_id == "women":
		product = Apparel.objects.get(id = product_id)
		photos = Picture.objects.filter(master_apparel_product = product_id).all()
		colors = Colors.objects.filter(master_apparel_product = product_id).all()
		sizes = Sizes.objects.filter(master_apparel_product = product_id).all()
		shipping = Shipping.objects.filter(master_apparel_product = product_id).all()
	if type_id == "kids":
		product = Apparel.objects.get(id = product_id)
		photos = Picture.objects.filter(master_apparel_product = product_id).all()
		colors = Colors.objects.filter(master_apparel_product = product_id).all()
		sizes = Sizes.objects.filter(master_apparel_product = product_id).all()
		shipping = Shipping.objects.filter(master_apparel_product = product_id).all()
	context = {
    "product" : product,
    "photos" : photos,
    "colors" : colors,
    "sizes" : sizes,
	"shipping" : shipping,
    }
	return render(request, 'main/productpage.html', context)

def promotions(request):
   return render(request, 'main/promotions.html')

def contact(request):
   return render(request, 'main/contact.html')

def createcontact(request):
	results = Contact.objects.createContact(request.POST)
	request.session['contactstatus'] = results['status']
	genErrors(request, results['errors'])
	return redirect('/contact')
