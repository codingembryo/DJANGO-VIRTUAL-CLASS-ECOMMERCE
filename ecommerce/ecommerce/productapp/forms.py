from django import forms
from .models import Product_table

class Product_form(forms.ModelForm):

    class Meta:
        model = Product_table
        fields = [

            'product_name',
            'price',
            'quantity',
            'category',
            'description',
            'product_picture',
        ]


        widgets = {
            'description':forms.Textarea(attrs={'cols':100, 'rows': 10})
        }