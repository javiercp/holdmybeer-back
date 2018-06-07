from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from chigre.models import KegType
from chigre.serializers import KegTypeSerializer


# Create your tests here.

class KegTypeCreateTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.data = {'name': 'Korny', 'size':'18.90', 'pints':'32', 'canyas':'53'}
           
    def test_create_kegtype(self):
        """
        Ensure we can create a new keg type object.
        """
        url = reverse('kegtype-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
class KegTypeReadTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.kegtype = KegType.objects.create(name='Korny', size=18.90, pints=32, canyas=53, creator=self.superuser)
          
    def test_read_kegtypes(self):
        """
        Ensure we can read keg types.
        """
        url = reverse('kegtype-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_read_kegtype(self):
        """
        Ensure we can read a keg type object.
        """
        url = reverse('kegtype-detail', args=[self.kegtype.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class KegTypeUpdateTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.kegtype = KegType.objects.create(name='kornelius', size=18.90, pints=32, canyas=53, creator=self.superuser)
        self.data = KegTypeSerializer(self.kegtype).data
        self.data.update({'name': 'Korny'})
          
    def test_update_kegtype(self):
        """
        Ensure we can update a keg type object.
        """
        url = reverse('kegtype-detail', args=[self.kegtype.id])
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class KegTypeDeleteTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.kegtype = KegType.objects.create(name='Korny', size=18.90, pints=32, canyas=53, creator=self.superuser)
          
    def test_delete_kegtype(self):
        """
        Ensure we can delete a keg type object.
        """
        url = reverse('kegtype-detail', args=[self.kegtype.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
