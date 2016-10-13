from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from payments.models import Payment

@login_required
@require_GET
def user_profile(request):
    payments = Payment.objects.filter(user=request.user).order_by('-date')
    return render(request, 'users/user_profile.html', context={
        'user': request.user,
        'payments': payments,
    })

