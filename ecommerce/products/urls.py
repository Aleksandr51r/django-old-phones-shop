from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductsListView.as_view(), name='shop'),
    path('about', views.about, name='about'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_page'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
