from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import Cart, CartItem
from products.models import Product
from django.views.generic import TemplateView, ListView, CreateView, DetailView


@login_required(login_url='users:login')
def profile_view(request):
    if not request.user.is_authenticated:
        return HttpResponse

# Create your views here.


class CartView(DetailView):
    template_name = 'cart/cart.html'
    context_object_name = 'cart'

    def get_object(self):
        return get_object_or_404(Cart, user=self.request.user)


# class CartView(DetailView):
#     template_name = 'cart/cart.html'
#     def get_queryset(self):
#         queryset = super(CartView, self).get_queryset()
#         user = self.kwargs.get('user')
#         return queryset.get(user=user)
#         template_name = 'cart/cart.html'
#     context_object_name = 'basket'
#     def get_context_data(self, **kwargs):
#         context = super(CartView, self).get_context_data(**kwargs)
#         context["baskets"] =  Cart.objects.filter(user=self.request.user)
#         return  context
#     def get_object(self):
#         return get_object_or_404(Cart, user=self.request.user)

@login_required
def add_cartitem(request, product_id):
    product = Product.objects.get(pk=product_id)
    
    cart = get_object_or_404(Cart, user=request.user)
    cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    
    cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cartitem.quantity += 1
        cartitem.save()
        
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def remove_cartitem(request, cartitem_id):
    cartitem = Cart.objects.get(pk=cartitem)
    cartitem.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# def add_to_cart(request, product_id):
#     cart = request.session.get('cart', {})   
#     cart[str(product_id)] = cart.get(str(product_id), 0) + 1  # +1 товар
#     request.session['cart'] = cart           
#     request.session.modified = True          
#     return redirect('cart_view')

# def cart_view(request):
#     cart = request.session.get('cart', {})
#     products = Product.objects.filter(id__in=cart.keys())
#     total = sum(p.price * cart[str(p.id)] for p in products)
#     return render(request, 'cart/view.html', {'products': products, 'cart': cart, 'total': total})


# def remove_from_cart(request, product_id):
#     cart = request.session.get('cart', {})
#     if str(product_id) in cart:
#         del cart[str(product_id)]
#         request.session['cart'] = cart
#         request.session.modified = True
#     return redirect('cart_view')
