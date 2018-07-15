from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from chigre.models import Secrets
from chigre.serializers import SecretsSerializer


# Create your tests here.        
class SecretsReadTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')

        self.secrets = Secrets.load()
        self.secrets.maps_key = '123'
        self.secrets.save()
                  
    def test_read_secrets(self):
        """
        Ensure we can read the secrets object.
        """
        url = reverse('secrets-info')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'maps_key': '123'})
        
class SecretsUpdateTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')

        self.secrets = Secrets.load()
        self.secrets.maps_key = '321'
        self.secrets.save()

        self.data = SecretsSerializer(self.secrets).data
        self.data.update({'maps_key': '123'})
          
    def test_update_secrets(self):
        """
        Ensure we can update the secrets object.
        """
        url = reverse('secrets-info')
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'maps_key': '123'})
     
class PubDeleteTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')

        self.secrets = Secrets.load()
        self.secrets.maps_key = '123'
        self.secrets.save()

        self.secrets.delete()
                  
    def test_read_secrets(self):
        """
        Ensure we can read the secrets object.
        """
        url = reverse('secrets-info')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'maps_key': '123'})
        