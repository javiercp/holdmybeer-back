from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from chigre.models import PubGallery
from chigre.serializers import PubGallerySerializer


# Create your tests here.

class PubGalleryCreateTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.data = {'title': 'photo', 'description':'great photo', 'image':'great.photo.jpg'}
           
    def test_create_photo(self):
        """
        Ensure we can create a new photo object.
        """
        url = reverse('gallery-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
class PubGalleryReadTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.photo = PubGallery.objects.create(title='photo', description='great photo', image='great.photo.jpg', creator=self.superuser)
          
    def test_read_photos(self):
        """
        Ensure we can read photos.
        """
        url = reverse('gallery-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_read_photo(self):
        """
        Ensure we can read a photo object.
        """
        url = reverse('gallery-detail', args=[self.photo.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class PubGalleryUpdateTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.photo = PubGallery.objects.create(title='foto', description='great photo', image='great.photo.jpg', creator=self.superuser)
        self.data = PubGallerySerializer(self.photo).data
        self.data.update({'title': 'photo'})
          
    def test_update_photo(self):
        """
        Ensure we can update a brewery object.
        """
        url = reverse('gallery-detail', args=[self.photo.id])
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BreweryDeleteTest(APITestCase): 
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.photo = PubGallery.objects.create(title='foto', description='great photo', image='great.photo.jpg', creator=self.superuser)
          
    def test_delete_photo(self):
        """
        Ensure we can delete a photo object.
        """
        url = reverse('gallery-detail', args=[self.photo.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
