from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import Product_form
from django.contrib import messages
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.urls import reverse
from .models import Product_table


# Create your views here.
@login_required
def uploadProduct(request):
    if request.method == "POST":
        product_form = Product_form(request.POST or None, request.FILES or None)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.user_id = request.user.id
            product.save()
            messages.success(request, ('Product uploaded successfully!'))
            return HttpResponseRedirect("display_product")
        else:
            messages.error(request, ('Please correct the error below.'))
            return HttpResponseRedirect("upload_product")

    else:
        product_form = Product_form
        return render(request, 'productapp/upload_product_form.html',{
            'product_form':product_form,
        })


def displayProduct(request):
    all_products = Product_table.objects.all()
    return render(request, 'productapp/display_product.html', {"all_products":all_products})
        

