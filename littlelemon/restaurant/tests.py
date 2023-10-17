from django.test import TestCase 
from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Menu
from .serializers import MenuSerializer
from django.urls import reverse

# class MenuViewTest(APITestCase):
    # def setUp(self):
    #     self.menu1 = Menu.objects.create(title="Dish 1", price=10.0, inventory=100)
    #     self.menu2 = Menu.objects.create(title="Dish 2", price=15.0, inventory=150)
    #     self.menu3 = Menu.objects.create(title="Dish 3", price=12.0, inventory=120)

    # def test_getall(self):
    #     url = reverse('menu')
    #     response = self.client.get(url)
    #     data = Menu.objects.all()
    #     serializer = MenuSerializer(data, many=True)
    #     self.assertEqual(response.data, serializer.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

class MenuItemTest(TestCase): 
     def test_get_item(self):
         item = Menu.objects.create(title="IceCream", price=80, inventory=100)
         self.assertEqual(str(item), "IceCream : 80")   