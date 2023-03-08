from itertools import product
from urllib import request

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Product


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account crested successfully!')
            return redirect('register')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def add_product(request):
    # Check if the form submitted has a method post
    if request.method == "POST":
        # Start receiving data from the form
        p_name = request.POST.get('jina')
        p_quantity = request.POST.get('kiasi')
        p_price = request.POST.get('bei')

        # Finally save the data in our table called products
        product = Product(prod_name=p_name, prod_quantity=p_quantity,
                          prod_price=p_price)
        product.save()
        # redirect back with a success message
        messages.success(request, 'Product saved successfully')
    return render(request, 'add-product.html')


@login_required
def view_products(request):
    # select all the products to be displayed
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


@login_required
def delete_product(request, id):
    # Fetch the product to be deleted
    product = Product.objects.get(id=id)
    product.delete()
    messages.success(request, 'product deleted successfully')
    return redirect('products')


@login_required
def update_product(request, id):
    # Fetch the product to be updated
    product = Product.objects.get(id=id)
    # Check if the form submitted has a method post
    if request.method == "POST":
        # Receive data from the form
        updated_name = request.POST.get('jina')
        updated_quantity = request.POST.get('kiasi')
        updated_price = request.POST.get('bei')

        # Update the product with he received update data
        product.prod_name = updated_name
        product.prod_quantity = updated_quantity
        product.prod_price = updated_price

        # Return the data back yo the database and redirect back
        # to product page with a success message
        product.save()
        messages.success(request, 'Product updated successfully')
        return redirect('products')
    return render(request, 'update-product.html', {'product': product})


@login_required
def payment(request, id):
    # Select the product to be paid
    product = Product.objects.get(id=id)
    return render(request, 'payment.html', {'product': product})
