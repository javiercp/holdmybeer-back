from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from chigre.models import Pub
from chigre.serializers import PubSerializer


# Create your tests here.        
class PubReadTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')

        self.pubinfo = Pub.load()
        self.pubinfo.name = 'Chigre'
        self.pubinfo.save()
                  
    def test_read_beertype(self):
        """
        Ensure we can read the pub info object.
        """
        url = reverse('pub-info')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'name': 'Chigre', 'motto': '', 'description': '', 'address': '', 'lat': None, 'lng': None, 'telephone': '', 'logo': ''})
        
class PubUpdateTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')

        self.pubinfo = Pub.load()
        self.pubinfo.name = 'Chigrin'
        self.pubinfo.save()

        self.data = PubSerializer(self.pubinfo).data
        self.data.update({'name': 'Chigre'})
          
    def test_update_beertype(self):
        """
        Ensure we can update the pub info object.
        """
        url = reverse('pub-info')
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'name': 'Chigre', 'motto': '', 'description': '', 'address': '', 'lat': None, 'lng': None, 'telephone': '', 'logo': ''})
     
class PubDeleteTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')

        self.pubinfo = Pub.load()
        self.pubinfo.name = 'Chigre'
        self.pubinfo.save()

        self.pubinfo.delete()
                  
    def test_read_beertype(self):
        """
        Ensure we can read the pub info object.
        """
        url = reverse('pub-info')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'name': 'Chigre', 'motto': '', 'description': '', 'address': '', 'lat': None, 'lng': None, 'telephone': '', 'logo': ''})
        