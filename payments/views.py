from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .forms import AddressForm 

@login_required
def address_capture(request):
    if request.method == 'GET':
        existing_address = request.user.addresses.first()
        print existing_address
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
