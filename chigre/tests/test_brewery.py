from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from chigre.models import Brewery
from chigre.serializers import BrewerySerializer


# Create your tests here.

class BreweryCreateTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.data = {'name': 'CamposBrew'}
           
    def test_create_brewery(self):
        """
        Ensure we can create a new brewery object.
        """
        url = reverse('brewery-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
class BreweryReadTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.brewery = Brewery.objects.create(name='CamposBrew', creator=self.superuser)
          
    def test_read_breweries(self):
        """
        Ensure we can read breweries.
        """
        url = reverse('brewery-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_read_brewery(self):
        """
        Ensure we can read a brewery object.
        """
        url = reverse('brewery-detail', args=[self.brewery.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class BreweryUpdateTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.brewery = Brewery.objects.create(name="CamposBru", creator=self.superuser)
        self.data = BrewerySerializer(self.brewery).data
        self.data.update({'name': 'CamposBrew'})
          
    def test_update_brewery(self):
        """
        Ensure we can update a brewery object.
        """
        url = reverse('brewery-detail', args=[self.brewery.id])
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BreweryDeleteTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.brewery = Brewery.objects.create(name="CamposBrew", creator=self.superuser)
          
    def test_delete_brewery(self):
        """
        Ensure we can delete a brewery object.
        """
        url = reverse('brewery-detail', args=[self.brewery.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
