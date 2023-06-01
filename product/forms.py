from django import forms

from product.models import Product


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']   #__all__

    def save(self, commit=True):
        # submit버튼을 눌렀을 때 작동
        new_product = Product.objects.create(
            name=self.cleaned_data.get('name'), # 사용자가 입력한 내용을 clean_name()으로 공백제거 가능
            price=self.cleaned_data.get('price'), # 사용자가 입력한 내용을 clean_name()으로 공백제거 가능
        )
        return new_product
