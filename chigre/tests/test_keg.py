from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from chigre.models import Keg
from chigre.serializers import KegSerializer
from chigre.models import KegType, Beer, Brewery, BeerType


# Create your tests here.

class KegCreateTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.brewery = Brewery.objects.create(name='CamposBrew', creator=self.superuser)
        self.beertype = BeerType.objects.create(name='brew')
        self.beer = Beer.objects.create(name='camposbrew', abv=7.6, brewery=self.brewery, beertype=self.beertype, creator=self.superuser)
        self.kegtype = KegType.objects.create(name='Korny', size=18.90, pints=32, canyas=53)       
        self.data = {'pintprice': 4.5, 'canyaprice':2.5, 'beer':self.beer.id, 'kegtype':self.beertype.id}
           
    def test_create_keg(self):
        """
        Ensure we can create a new keg object.
        """
        url = reverse('keg-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
class KegReadTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.brewery = Brewery.objects.create(name='CamposBrew', creator=self.superuser)
        self.beertype = BeerType.objects.create(name='brew')
        self.beer = Beer.objects.create(name='camposbrew', abv=7.6, brewery=self.brewery, beertype=self.beertype, creator=self.superuser)
        self.kegtype = KegType.objects.create(name='Korny', size=18.90, pints=32, canyas=53)       
        self.keg = Keg.objects.create(pintprice=7.6, canyaprice=3.5, beer=self.beer, kegtype=self.kegtype, creator=self.superuser)
          
    def test_read_kegs(self):
        """
        Ensure we can read kegs.
        """
        url = reverse('keg-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_read_keg(self):
        """
        Ensure we can read a keg object.
        """
        url = reverse('keg-detail', args=[self.keg.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class KegUpdateTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.brewery = Brewery.objects.create(name='CamposBrew', creator=self.superuser)
        self.beertype = BeerType.objects.create(name='brew')
        self.beer = Beer.objects.create(name='camposbrew', abv=7.6, brewery=self.brewery, beertype=self.beertype, creator=self.superuser)
        self.kegtype = KegType.objects.create(name='Korny', size=18.90, pints=32, canyas=53)       
        self.keg = Keg.objects.create(pintprice=17.6, canyaprice=3.5, beer=self.beer, kegtype=self.kegtype, creator=self.superuser)
        self.data = KegSerializer(self.keg).data
        self.data.update({'pintprice': 7.6})
          
    def test_update_keg(self):
        """
        Ensure we can update a keg object.
        """
        url = reverse('keg-detail', args=[self.keg.id])
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class KegDeleteTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.brewery = Brewery.objects.create(name='CamposBrew', creator=self.superuser)
        self.beertype = BeerType.objects.create(name='brew')
        self.beer = Beer.objects.create(name='camposbrew', abv=7.6, brewery=self.brewery, beertype=self.beertype, creator=self.superuser)
        self.kegtype = KegType.objects.create(name='Korny', size=18.90, pints=32, canyas=53)       
        self.keg = Keg.objects.create(pintprice=17.6, canyaprice=3.5, beer=self.beer, kegtype=self.kegtype, creator=self.superuser)
             
    def test_delete_keg(self):
        """
        Ensure we can delete a keg object.
        """
        url = reverse('keg-detail', args=[self.keg.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
