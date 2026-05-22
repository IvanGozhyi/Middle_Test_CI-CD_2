from django.test import TestCase
from django.urls import reverse
from .models import Category, Recipe


class RecipeViewsTest(TestCase):
    def setUp(self):
        self.category_breakfast = Category.objects.create(name='Breakfast')
        self.category_main = Category.objects.create(name='Main Courses')

        for i in range(6):
            Recipe.objects.create(
                title=f'Breakfast Recipe {i}',
                description='Test description',
                instructions='Test instructions',
                ingredients='Test ingredients',
                category=self.category_breakfast,
            )

        for i in range(2):
            Recipe.objects.create(
                title=f'Main Course Recipe {i}',
                description='Test description',
                instructions='Test instructions',
                ingredients='Test ingredients',
                category=self.category_main,
            )

    def test_main_view(self):
        response = self.client.get(reverse('recipe:main'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertIn('recipes', response.context)
        self.assertEqual(len(response.context['recipes']), 5)

    def test_category_list_view(self):
        response = self.client.get(reverse('recipe:category_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')
        self.assertIn('categories', response.context)

        categories = response.context['categories']
        self.assertEqual(len(categories), 2)

        for category in categories:
            if category.name == 'Breakfast':
                self.assertEqual(category.recipe_count, 6)
            elif category.name == 'Main Courses':
                self.assertEqual(category.recipe_count, 2)
# Create your tests here.
