from django import template
import braintree
from django.conf import settings

register = template.Library()

@register.inclusion_tag('payments/buy_now_button.html', takes_context=True)
def buy_now_button(context):

    user = context.request.user
    has_account = user.is_authenticated()
    has_address = user.is_authenticated() and user.addresses.exists()

    if has_account and has_address:
        braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id=settings.BRAINTREE_MERCHANT_ID,
                                  public_key=settings.BRAINTREE_PUBLIC_KEY,
                                  private_key=settings.BRAINTREE_PRIVATE_KEY)
        token = braintree.ClientToken.generate()

    else:
        token = "It wasn't working"


    return {
        'has_account': has_account,
        'has_address': has_address,
        'next': context.request.get_full_path(),
        'braintree_token': token,
        'product': context['product']
    }