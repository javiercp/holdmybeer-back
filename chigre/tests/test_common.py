from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from chigre.models import Brewery
from chigre.serializers import BrewerySerializer


# Create your tests here.

class CreatorDeleteTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.brewery = Brewery.objects.create(name="CamposBrew", country='ES', creator=self.superuser)
          
    def test_delete_brewerycreator(self):
        """
        Ensure we can delete a creator object and retrieve data.
        """
        self.client.logout()
        self.superuser.delete()
        
        url = reverse('brewery-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
