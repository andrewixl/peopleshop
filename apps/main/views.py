from django.shortcuts import render, redirect, HttpResponse
from .models import Apparel_Product, Apparel_Picture, Apparel_Colors, Apparel_Sizes, Contact
from django.contrib import messages

# Create your views here.
def genErrors(request, Emessages):
	for message in Emessages:
		messages.error(request, message)

def index(request):
    return render(request, 'main/index.html')

def categories(request, id):
    if id == "apparel":
        products = Apparel_Product.objects.all()
    if id == "books":
        products = Apparel_Product.objects.all()
    if id == "electronics":
        products = Apparel_Product.objects.all()

    context = {
    "products":products,
    }
    return render(request, 'main/categories.html', context)

def product(request, type_id, product_id):
    if type_id == "apparel":
        product = Apparel_Product.objects.get(id = product_id)
        photos = Apparel_Picture.objects.filter(master_apparel_product = product_id).all()
        colors = Apparel_Colors.objects.filter(master_apparel_product = product_id).all()
        sizes = Apparel_Sizes.objects.filter(master_apparel_product = product_id).all()
    context = {
    "product" : product,
    "photos" : photos,
    "colors" : colors,
    "sizes" : sizes,
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
