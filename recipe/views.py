from django.shortcuts import render
from django.db.models import Count
from .models import Recipe, Category


def main(request):

    latest_recipes = Recipe.objects.order_by('-created_at')[:5]


    return render(request, 'main.html', {'recipes': latest_recipes})

def category_list(request):

    categories = Category.objects.annotate(recipe_count=Count('recipe'))

    return render(request, 'category_list.html', {'categories': categories})
