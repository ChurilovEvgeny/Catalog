from django import forms
from django.forms import HiddenInput

from catalog.models import Product, ProductVersion


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['owner'].widget = HiddenInput()

    forbidden_words = (
        "казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар")

    def clean_name(self):
        return self.__validate_by_forbidden_words(self.cleaned_data.get('name'), "Имя")

    def clean_description(self):
        return self.__validate_by_forbidden_words(self.cleaned_data.get('description'), "Описание")

    def __validate_by_forbidden_words(self, cleaned_data, field_name_exception_message):
        prepare_data = cleaned_data.strip().lower()
        for forbidden in self.forbidden_words:
            if forbidden in prepare_data:
                raise forms.ValidationError(
                    f"{field_name_exception_message} не должно содержать запрещенные слова '{forbidden}'!")
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
