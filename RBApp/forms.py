from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields  = '__all__'


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'


class MenuTypeForm(forms.ModelForm):
    class Meta:
        model = MenuType
        fields = '__all__'
        



