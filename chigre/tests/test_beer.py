from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from chigre.models import Beer
from chigre.serializers import BeerSerializer
from chigre.models import BeerType
from chigre.models import Brewery


# Create your tests here.

class BeerCreateTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.brewery = Brewery.objects.create(name='CamposBrew', country='ES', creator=self.superuser)
        self.beertype = BeerType.objects.create(name='brew')
        self.data = {'name': 'camposbrew', 'description':'great brew', 'abv':7.5, 'brewery':self.brewery.id, 'beertype':self.beertype.id}
           
    def test_create_beer(self):
        """
        Ensure we can create a new beer object.
        """
        url = reverse('beer-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
class BeerReadTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.brewery = Brewery.objects.create(name='CamposBrew', country='ES', creator=self.superuser)
        self.beertype = BeerType.objects.create(name='brew')
        self.beer = Beer.objects.create(name='camposbrew', abv=7.6, brewery=self.brewery, beertype=self.beertype, creator=self.superuser)
          
    def test_read_beers(self):
        """
        Ensure we can read beers.
        """
        url = reverse('beer-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_read_beer(self):
        """
        Ensure we can read a beer object.
        """
        url = reverse('beer-detail', args=[self.beer.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_read_beer_ex(self):
        """
        Ensure we can read a beer object with all data.
        """
        url = reverse('beer-detail-ex', args=[self.beer.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class BeerUpdateTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.brewery = Brewery.objects.create(name='CamposBrew', country='ES', creator=self.superuser)
        self.beertype = BeerType.objects.create(name='brew')
        self.beer = Beer.objects.create(name='camposbru', abv=7.6, brewery=self.brewery, beertype=self.beertype, creator=self.superuser)
        self.data = BeerSerializer(self.beer).data
        self.data.update({'name': 'camposbrew'})
          
    def test_update_beer(self):
        """
        Ensure we can update a beer object.
        """
        url = reverse('beer-detail', args=[self.beer.id])
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BeerDeleteTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.brewery = Brewery.objects.create(name='CamposBrew', country='ES', creator=self.superuser)
        self.beertype = BeerType.objects.create(name='brew')
        self.beer = Beer.objects.create(name='camposbrew', abv=7.8, brewery=self.brewery, beertype=self.beertype, creator=self.superuser)
          
    def test_delete_beer(self):
        """
        Ensure we can delete a beer object.
        """
        url = reverse('beer-detail', args=[self.beer.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
