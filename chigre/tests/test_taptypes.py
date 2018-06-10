from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from chigre.models import TapType
from chigre.serializers import TapTypeSerializer


# Create your tests here.

class TapTypeCreateTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.data = {'name': 'simple tap'}
           
    def test_create_taptype(self):
        """
        Ensure we can create a new tap type object.
        """
        url = reverse('taptype-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
class TapTypeReadTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.taptype = TapType.objects.create(name='simple tap')
          
    def test_read_taptypes(self):
        """
        Ensure we can read tap types.
        """
        url = reverse('taptype-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_read_taptype(self):
        """
        Ensure we can read a tap type object.
        """
        url = reverse('taptype-detail', args=[self.taptype.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class TapTypeUpdateTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.taptype = TapType.objects.create(name='complex tap')
        self.data = TapTypeSerializer(self.taptype).data
        self.data.update({'name': 'simple tap'})
          
    def test_update_taptype(self):
        """
        Ensure we can update a tap type object.
        """
        url = reverse('taptype-detail', args=[self.taptype.id])
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TapTypeDeleteTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.taptype = TapType.objects.create(name='simple tap')
          
    def test_delete_taptype(self):
        """
        Ensure we can delete a tap type object.
        """
        url = reverse('taptype-detail', args=[self.taptype.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
