from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .forms import AddressForm
from django.http import HttpResponseBadRequest
import braintree
from collection.models import Products
from django.conf import settings 
from .models import Payment
from datetime import datetime

@login_required
def address_capture(request):
    if request.method == 'GET':
        existing_address = request.user.addresses.first()
        form = AddressForm(instance=existing_address)

    elif request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            
            address.user = request.user

            existing_address = request.user.addresses.first()
            if existing_address:
                address.id = existing_address.id 

            address.save()
            return redirect(request.GET.get("next", reverse('catalog')))

    
    return render(request, 'payments/address_form.html', context={
        'form': form,
        
    })

@login_required
def checkout(request):
    if request.method == 'POST':
        braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id=settings.BRAINTREE_MERCHANT_ID,
                                  public_key=settings.BRAINTREE_PUBLIC_KEY,
                                  private_key=settings.BRAINTREE_PRIVATE_KEY)
        token = braintree.ClientToken.generate()
        product = Products.objects.get(id=request.POST['product_id'])
        nonce = request.POST['payment_method_nonce']
        result = braintree.Transaction.sale({
            'amount': str(product.price),
            'payment_method_nonce': nonce,
            'options':{
            'submit_for_settlement': True
            }
        })
        if result.is_success:
            payment = Payment.objects.create(
                user=request.user, 
                date=result.transaction.created_at, 
                transaction_id=result.transaction.id, 
                product=product, 
                status='succesful', 
            )
            return redirect("/")
        else:
            payment = Payment.objects.create(
                user=request.user, 
                date=datetime.now(),  
                product=product, 
                status='fail', 
            )
            return redirect("/")


    else:
        return HttpResponseBadRequest()

