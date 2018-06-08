from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from chigre.models import BeerType
from chigre.serializers import BeerTypeSerializer


# Create your tests here.

class BeerTypeCreateTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.data = {'name': 'brew', 'description':'great brew'}
           
    def test_create_beertype(self):
        """
        Ensure we can create a new beer type object.
        """
        url = reverse('beertype-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
class BeerTypeReadTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.beertype = BeerType.objects.create(name='brew')
          
    def test_read_beertypes(self):
        """
        Ensure we can read beer types.
        """
        url = reverse('beertype-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_read_kegtype(self):
        """
        Ensure we can read a beer type object.
        """
        url = reverse('beertype-detail', args=[self.beertype.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class BeerTypeUpdateTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.beertype = BeerType.objects.create(name='bru', description='great brew')
        self.data = BeerTypeSerializer(self.beertype).data
        self.data.update({'name': 'brew'})
          
    def test_update_beertype(self):
        """
        Ensure we can update a beer type object.
        """
        url = reverse('beertype-detail', args=[self.beertype.id])
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BeerTypeDeleteTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.beertype = BeerType.objects.create(name='brew')
          
    def test_delete_kegtype(self):
        """
        Ensure we can delete a beer type object.
        """
        url = reverse('beertype-detail', args=[self.beertype.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
