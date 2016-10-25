from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from payments.models import Payment
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

@login_required
@require_GET
def user_profile(request):
    payments = Payment.objects.filter(user=request.user).order_by('-date')
    return render(request, 'users/user_profile.html', context={
        'user': request.user,
        'payments': payments,
    })

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                '%s: %s' %(form.cleaned_data['email'], form.cleaned_data['subject']),
                form.cleaned_data['message'],
                'contact@yosola.co',
                settings.ADMINS,
                fail_silently=False,
                )
            return redirect("/")
    else:
        form = ContactForm()

    return render(request, 'contact.html', context={
        'form': form,
        })

