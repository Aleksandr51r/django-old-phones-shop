from django.db.models import Prefetch
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Product, Category, Tag, ProductImage, PhoneSpecs
from .forms import SearchForm


class ProductsListView(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related(
            Prefetch('images', queryset=ProductImage.objects.order_by(
                '-is_main', 'id'))
        )
        release_year = self.request.GET.getlist('release_year')
        release_year = [int(year) for year in release_year if year.isdigit()]

        for i in release_year:
            print(type(i))

        filters = {
            'brand__id__in': self.request.GET.getlist('brand'),
            'release_year__in': release_year,
        }

        for key, value in filters.items():
            if value:
                queryset = queryset.filter(**{key: value})

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.request.GET.copy()
        if 'release_year' in data:
            data.setlist('release_year', [int(x) for x in data.getlist(
                'release_year') if x.isdigit()])
        context['form'] = SearchForm(data)
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        slug = self.kwargs.get('slug')
        product = get_object_or_404(
            Product.objects.prefetch_related('images'),
            slug=slug
        )
        context['products'] = product
        return context


def about(request):
    return HttpResponse("about")
