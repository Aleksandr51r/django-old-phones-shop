from django import template

register = template.Library()


@register.inclusion_tag('products/product_card.html', takes_context=True)
def get_product_card(context, prod):
    return {'product': prod}

