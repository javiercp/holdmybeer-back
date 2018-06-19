from django.test import TestCase
from django.contrib.auth.models import User
from chigre.models import Brewery
from chigre.serializers import BrewerySerializer
from chigreQL.schema import Query
import graphene

# Create your tests here.

class BreweryReadTest(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.brewery = Brewery.objects.create(name='CamposBrew', country='ES', creator=self.superuser)
          
    def test_read_breweries(self):
        """
        Ensure we can read breweries.
        """

        schema = graphene.Schema(query=Query)
        query = '''
        {
            allBreweries {
                edges {
                    node {
                        name
                    }
                }
            }
        }
        '''
        expected = {
            "allBreweries": {
                "edges": [
                    {
                        "node": {
                            "name": "CamposBrew"
                        }
                    }
                ]
            }
        }
        result = schema.execute(query)
        assert not result.errors
        assert result.data == expected 
