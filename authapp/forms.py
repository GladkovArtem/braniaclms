from django.contrib.auth import get_user_model
# from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

# class StyleFormMixin:
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             if isinstance(field.Widget, forms.Widget.CheckboxInput):
#                 field.Widget.attrs['class'] = 'form-check-input'
#             elif isinstance(field.Widget, forms.DateTimeInput):
#                 field.Widget.attrs['class'] = 'form-control flatpickr-basic'
#             elif isinstance(field.Widget, forms.TimeInput):
#                 field.Widget.attrs['class'] = 'form-control flatpickr-time'
#             elif isinstance(field.Widget, forms.Widgets.SelectMultiple):
#                 field.Widget.attrs['class'] = 'select2 form-control select2-multiple'
#             else:
#                 field.Widget.attrs['class'] = 'form-control'


# class CustomUserCreationForm(StyleFormMixin, UserCreationForm):
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
            'first_name',
            'age',
            'avatar'
        )

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if 100 < age < 18:
            raise ValueError('Вы слишком молоды для этого сайта')
        return age


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
            'first_name',
            'age',
            'avatar'
        )

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if 100 < age < 18:
            raise ValueError('Вы слишком молоды для этого сайта')
        return age