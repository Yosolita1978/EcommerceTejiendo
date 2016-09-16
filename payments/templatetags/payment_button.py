from django import template

register = template.Library()

@register.inclusion_tag('payments/buy_now_button.html', takes_context=True)
def buy_now_button(context):
    user = context.request.user

    print user.is_authenticated() and user.addresses.exists()

    return {
        'has_account': user.is_authenticated(),
        'has_address': user.is_authenticated() and user.addresses.exists(),
        'next': context.request.get_full_path(),

    }