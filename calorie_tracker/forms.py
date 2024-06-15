
from django import forms
from .models import FoodItem

class FoodItemForm(forms.ModelForm):
    name = forms.TextInput()
    calories = forms.IntegerField()
    class Meta:
        model = FoodItem
        fields = ['name', 'calories']        