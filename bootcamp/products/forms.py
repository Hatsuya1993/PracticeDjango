from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={"placeholder": "Your title"}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "placeholder": "Your description",
            "class": "new-class-name two",
            "id": "my-id-for-textarea",
            "row": 20,
            "cols": 120
        }
    ))
    price = forms.DecimalField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not("CFE" in title):
            raise forms.ValidationError("This is not valid")
        return title


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={"placeholder": "Your title"}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "placeholder": "Your description",
            "class": "new-class-name two",
            "id": "my-id-for-textarea",
            "row": 20,
            "cols": 120
        }
    ))
    price = forms.DecimalField()
