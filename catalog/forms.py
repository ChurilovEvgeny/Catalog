from django import forms

from catalog.models import Product


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
