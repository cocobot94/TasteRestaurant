from django import forms
from .models import Products


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ["name", "image", "description", "price", "menu", "category_product"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(),
            "menu": forms.RadioSelect(),
            "category_product": forms.SelectMultiple,
        }
