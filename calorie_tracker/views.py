from django.shortcuts import render, redirect
from .models import FoodItem
from django.utils import timezone
from .forms import FoodItemForm
def index(request):
    items = FoodItem.objects.all()
    total_calories = sum(item.calories for item in items)
    return render(request, 'index.html', {'items': items, 'total_calories': total_calories})
def home(request):
    items = FoodItem.objects.filter()
    total_calories = sum(item.calories for item in items)
    return render(request, 'index.html', {'items': items, 'total_calories': total_calories})
def food(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FoodItemForm()
    return render(request, 'food.html', {'form': form})
def delete_food_item(request, item_id):
    item = FoodItem.objects.get(id=item_id)
    item.delete()
    return redirect(request, 'index')
def reset_calories(request):
    FoodItem.objects.filter().delete()
    return redirect(request, 'index')



