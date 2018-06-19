import graphene

from django.test import TestCase
from django.contrib.auth.models import User
from chigre.models import Brewery, BeerType, KegType, TapType, Beer, Keg, Tap
from chigreQL.schema import Query

# Create your tests here.

def test_query(query, expected):
    schema = graphene.Schema(query=Query)
    result = schema.execute(query)
    assert not result.errors
    assert result.data == expected 

class BreweryReadTest(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.brewery = Brewery.objects.create(name='CamposBrew', country='ES', creator=self.superuser)
          
    def test_read_breweries(self):
        """
        Ensure we can read breweries.
        """
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
        test_query(query, expected)

class BeerTypeReadTest(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.beertype = BeerType.objects.create(name='brew')

    def test_read_beertypes(self):
        """
        Ensure we can read beer types.
        """
        query = '''
        {
            allBeertypes {
                edges {
                    node {
                        name
                    }
                }
            }
        }
        '''
        expected = {
            "allBeertypes": {
                "edges": [
                    {
                        "node": {
                            "name": "brew"
                        }
                    }
                ]
            }
        }
        test_query(query, expected)

class KegTypeReadTest(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.kegtype = KegType.objects.create(name='Korny', size=18.90, pints=32, canyas=53)
          
    def test_read_kegtypes(self):
        """
        Ensure we can read keg types.
        """
        query = '''
        {
            allKegtypes {
                edges {
                    node {
                        name
                    }
                }
            }
        }
        '''
        expected = {
            "allKegtypes": {
                "edges": [
                    {
                        "node": {
                            "name": "Korny"
                        }
                    }
                ]
            }
        }
        test_query(query, expected)

class TapTypeReadTest(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.taptype = TapType.objects.create(name='simple tap')
          
    def test_read_taptypes(self):
        """
        Ensure we can read tap types.
        """
        query = '''
        {
            allTaptypes {
                edges {
                    node {
                        name
                    }
                }
            }
        }
        '''
        expected = {
            "allTaptypes": {
                "edges": [
                    {
                        "node": {
                            "name": "simple tap"
                        }
                    }
                ]
            }
        }
        test_query(query, expected)

class BeerReadTest(TestCase):
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
        query = '''
        {
            allBeers {
                edges {
                    node {
                        name
                    }
                }
            }
        }
        '''
        expected = {
            "allBeers": {
                "edges": [
                    {
                        "node": {
                            "name": "camposbrew"
                        }
                    }
                ]
            }
        }
        test_query(query, expected)

class KegReadTest(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.brewery = Brewery.objects.create(name='CamposBrew', country='ES', creator=self.superuser)
        self.beertype = BeerType.objects.create(name='brew')
        self.beer = Beer.objects.create(name='camposbrew', abv=7.6, brewery=self.brewery, beertype=self.beertype, creator=self.superuser)
        self.kegtype = KegType.objects.create(name='Korny', size=18.90, pints=32, canyas=53)       
        self.keg = Keg.objects.create(pintprice=7.6, canyaprice=3.5, beer=self.beer, kegtype=self.kegtype, creator=self.superuser)
          
    def test_read_kegs(self):
        """
        Ensure we can read kegs.
        """
        query = '''
        {
            allKegs {
                edges {
                    node {
                        pintprice
                    }
                }
            }
        }
        '''
        expected = {
            "allKegs": {
                "edges": [
                    {
                        "node": {
                            "pintprice": 7.6
                        }
                    }
                ]
            }
        }
        test_query(query, expected)

class TapReadTest(TestCase):
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
        query = '''
        {
            allTaps {
                edges {
                    node {
                        number
                    }
                }
            }
        }
        '''
        expected = {
            "allTaps": {
                "edges": [
                    {
                        "node": {
                            "number": 1
                        }
                    }
                ]
            }
        }
        test_query(query, expected)
