from django import forms
from .models import *


class UserForm(forms.ModelForm):
    def save(self, password, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(password)
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields  = '__all__'

    

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ('name', 'price', 'description')
        # fields = '__all__'


class MenuTypeForm(forms.ModelForm):
    class Meta:
        model = MenuType
        fields = ('name', 'description')

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('username', 'total_price')
        


