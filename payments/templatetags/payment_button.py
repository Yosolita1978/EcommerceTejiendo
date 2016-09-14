from django import template

register = template.Library()

@register.inclusion_tag('payments/buy_now_button.html', takes_context=True)
def buy_now_button(context):
    user = context.request.user

    return {
        'ready_to_buy': user.is_authenticated(),
        'next': context.request.get_full_path(),
    }