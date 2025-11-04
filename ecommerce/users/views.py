from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import UserRegistrationForm, UserLoginForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import auth
from users.models import User
from cart.models import Cart

# Create your views here.class MyView(View):


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            Cart.objects.create(user=user)
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    print(request.POST)
    context = {'form': form}
    return render(request, template_name='users/registration.html', context=context)


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('users:profile')


def profile(request):
    return render(request, template_name='users/profile.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('products:shop'))


class Logout(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='users/logout.html')


class UserProfileView(UpdateView):
    model = User
    # form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:login')

    def get_succsess_url(self):
        return reverse_lazy('users:profile', args=self.object.id)
