from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from chigre.models import Tap
from chigre.serializers import TapSerializer
from chigre.models import Keg, KegType, Beer, Brewery, BeerType, TapType


# Create your tests here.

class TapCreateTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        
        self.brewery = Brewery.objects.create(name='CamposBrew', country='ES', creator=self.superuser)
        self.beertype = BeerType.objects.create(name='brew')
        self.beer = Beer.objects.create(name='camposbrew', abv=7.6, brewery=self.brewery, beertype=self.beertype, creator=self.superuser)
        self.kegtype = KegType.objects.create(name='Korny', size=18.90, pints=32, canyas=53)
        self.keg = Keg.objects.create(pintprice=7.6, canyaprice=3.5, beer=self.beer, kegtype=self.kegtype, creator=self.superuser)
        self.taptype = TapType.objects.create(name='simple tap')
        
        self.data = {'number': 1, 'keg':self.keg.id, 'taptype':self.taptype.id}
           
    def test_create_tap(self):
        """
        Ensure we can create a new tap object.
        """
        url = reverse('tap-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
class TapReadTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        
        self.brewery = Brewery.objects.create(name='CamposBrew', country='ES', creator=self.superuser)
        self.beertype = BeerType.objects.create(name='brew')
        self.beer = Beer.objects.create(name='camposbrew', abv=7.6, brewery=self.brewery, beertype=self.beertype, creator=self.superuser)
        self.kegtype = KegType.objects.create(name='Korny', size=18.90, pints=32, canyas=53)
        self.keg = Keg.objects.create(pintprice=7.6, canyaprice=3.5, beer=self.beer, kegtype=self.kegtype, creator=self.superuser)
        self.taptype = TapType.objects.create(name='simple tap')
        
        self.tap = Tap.objects.create(number=1, keg=self.keg, taptype=self.taptype, creator=self.superuser)
          
    def test_read_taps(self):
        """
        Ensure we can read taps.
        """
        url = reverse('tap-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_read_taps_ex(self):
        """
        Ensure we can read taps with all data.
        """
        url = reverse('tap-list-ex')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_read_tap(self):
        """
        Ensure we can read a tap object.
        """
        url = reverse('tap-detail', args=[self.tap.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_read_tap_ex(self):
        """
        Ensure we can read a tap object with all data.
        """
        url = reverse('tap-detail-ex', args=[self.tap.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class TapUpdateTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        
        self.brewery = Brewery.objects.create(name='CamposBrew', country='ES', creator=self.superuser)
        self.beertype = BeerType.objects.create(name='brew')
        self.beer = Beer.objects.create(name='camposbrew', abv=7.6, brewery=self.brewery, beertype=self.beertype, creator=self.superuser)
        self.kegtype = KegType.objects.create(name='Korny', size=18.90, pints=32, canyas=53)
        self.keg = Keg.objects.create(pintprice=7.6, canyaprice=3.5, beer=self.beer, kegtype=self.kegtype, creator=self.superuser)
        self.taptype = TapType.objects.create(name='simple tap')
        
        self.tap = Tap.objects.create(number=2, keg=self.keg, taptype=self.taptype, creator=self.superuser)
        self.data = TapSerializer(self.tap).data
        self.data.update({'number': 1})
          
    def test_update_tap(self):
        """
        Ensure we can update a tap object.
        """
        url = reverse('tap-detail', args=[self.tap.id])
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TapDeleteTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        
        self.brewery = Brewery.objects.create(name='CamposBrew', country='ES', creator=self.superuser)
        self.beertype = BeerType.objects.create(name='brew')
        self.beer = Beer.objects.create(name='camposbrew', abv=7.6, brewery=self.brewery, beertype=self.beertype, creator=self.superuser)
        self.kegtype = KegType.objects.create(name='Korny', size=18.90, pints=32, canyas=53)
        self.keg = Keg.objects.create(pintprice=7.6, canyaprice=3.5, beer=self.beer, kegtype=self.kegtype, creator=self.superuser)
        self.taptype = TapType.objects.create(name='simple tap')
        
        self.tap = Tap.objects.create(number=1, keg=self.keg, taptype=self.taptype, creator=self.superuser)
             
    def test_delete_tap(self):
        """
        Ensure we can delete a tap object.
        """
        url = reverse('tap-detail', args=[self.tap.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
