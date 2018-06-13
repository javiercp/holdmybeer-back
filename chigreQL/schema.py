import graphene

from graphene import Node, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from chigre.models import Brewery, BeerType, KegType, Beer, Keg, TapType, Tap

class BreweryNode(DjangoObjectType):
    class Meta:
        model = Brewery
        filter_fields = {
            'name': ['exact','istartswith', 'icontains'],
            'description': ['istartswith', 'icontains'],
            'country': ['exact'],
            }
        interfaces = (Node, )

class Query(ObjectType):    
    breweries = Node.Field(BreweryNode)
    all_breweries = DjangoFilterConnectionField(BreweryNode)
        
schema = graphene.Schema(
    query=Query,
)
