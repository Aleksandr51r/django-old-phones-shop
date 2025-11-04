

navmenu = [
    {'title': 'About', 'url_name': 'products:about'},
    {'title': 'Catalog', 'url_name': 'products:shop'},
    {'title': 'Cart', 'url_name': 'cart:cart'},
    # {'title': 'Orders', 'url_name': 'orders:orders'},
    {'title': 'Account', 'url_name': 'users:login'}
]


def get_nav_menu(request):
    return {"get_nav_menu": navmenu}
