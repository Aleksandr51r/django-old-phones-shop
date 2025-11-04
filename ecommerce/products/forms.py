from .models import Product, Brand
from django import forms


class SearchForm(forms.Form):

    brand = forms.ModelMultipleChoiceField(queryset=Brand.objects.all(
    ), widget=forms.CheckboxSelectMultiple(attrs={'class': 'content__brand-checkbox'}), required=False,)
    release_year = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'type': 'range',  
            'min': '1995',
            'max': '2010',
            'step': '1',
            'class': 'content__year-slider'
        }),
        required=False,
        min_value=1995,
        max_value=2010
    )

    # price_min = forms.DecimalField(required=False)
    # price_max = forms.DecimalField(required=False)

    # def clen_relise_year():
    #     year = self.cleaned data

    #     if 2000 > relise_year > 2010:
    #         raise ValueError
