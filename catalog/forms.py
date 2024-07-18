from django import forms

from catalog.models import Product, ProductVersion


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        prepare_data = cleaned_data.strip().lower()
        forbidden_words = (
            "казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар")
        for forbidden in forbidden_words:
            if forbidden in prepare_data:
                raise forms.ValidationError(f"Имя не должно содержать запрещенные слова '{forbidden}'!")

        return cleaned_data


class ProductVersionForm(forms.ModelForm):
    class Meta:
        model = ProductVersion
        fields = '__all__'

    def clean_is_active(self):
        cleaned_data = self.cleaned_data.get('is_active')
        # ver = self.cleaned_data.get('version')
        # if cleaned_data:
        #     data = ProductVersion.objects.filter(product=self.instance.product, is_active=True).exclude(version=ver)
        #     if data.exists():
        #         print("raise")
        #         raise forms.ValidationError("Для данного продукта уже есть активная версия!")

        return cleaned_data
