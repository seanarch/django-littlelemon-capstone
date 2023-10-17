from django.test import TestCase 
from restaurant.models import Menu 
from restaurant.views import MenuItemView
from rest_framework import serializers 
from rest_framework.test import APIRequestFactory


class MenuViewTest(TestCase): 
    def setup(self): 
        self.menu1 = Menu.objects.create(name="Dish 1", price=10.0)
        self.menu2 = Menu.objects.create(name="Dish 2", price=15.0)
        self.menu3 = Menu.objects.create(name="Dish 3", price=12.0)        

    def test_getall(self): 
        factory = APIRequestFactory()
        request = factory.get('/restaurant/menus/')   
        response = MenuItemView.as_view()(request)
 
        serialized_data = serializers.serialize('json', [self.menu1, self.menu2, self.menu3])
 
        self.assertJSONEqual(str(response.content, encoding='utf8'), serialized_data)