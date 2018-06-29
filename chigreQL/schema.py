import graphene

from graphene import Node, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation

from chigre.models import Brewery, BeerType, KegType, Beer, Keg, TapType, Tap, Pub
from chigre.serializers import BrewerySerializer

class BreweryNode(DjangoObjectType):
    class Meta:
        model = Brewery
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'description': ['istartswith', 'icontains'],
            'country': ['exact'],
            }
        interfaces = (Node, )

class BeerTypeNode(DjangoObjectType):
    class Meta:
        model = BeerType
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'description': ['istartswith', 'icontains'],
            }
        interfaces = (Node, )

class KegTypeNode(DjangoObjectType):
    class Meta:
        model = KegType
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'size': ['exact'],
            }
        interfaces = (Node, )

class TapTypeNode(DjangoObjectType):
    class Meta:
        model = TapType
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            }
        interfaces = (Node, )

class BeerNode(DjangoObjectType):
    class Meta:
        model = Beer
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'description': ['istartswith', 'icontains'],
            }
        interfaces = (Node, )

class KegNode(DjangoObjectType):
    class Meta:
        model = Keg
        filter_fields = {
            }
        interfaces = (Node, )

class TapNode(DjangoObjectType):
    class Meta:
        model = Tap
        filter_fields = {
            'number': ['exact'],
            }
        interfaces = (Node, )

class PubNode(DjangoObjectType):
    class Meta:
        model = Pub
        exclude_fields = ('id')

class Query(ObjectType):
    pub_info = graphene.Field(PubNode)
    breweries = Node.Field(BreweryNode)
    all_breweries = DjangoFilterConnectionField(BreweryNode)
    beertypes = Node.Field(BeerTypeNode)
    all_beertypes = DjangoFilterConnectionField(BeerTypeNode)
    kegtypes = Node.Field(KegTypeNode)
    all_kegtypes = DjangoFilterConnectionField(KegTypeNode)
    taptypes = Node.Field(TapTypeNode)
    all_taptypes = DjangoFilterConnectionField(TapTypeNode)
    beers = Node.Field(BeerNode)
    all_beers = DjangoFilterConnectionField(BeerNode)
    kegs = Node.Field(KegNode)
    all_kegs = DjangoFilterConnectionField(KegNode)
    taps = Node.Field(TapNode)
    all_taps = DjangoFilterConnectionField(TapNode)

    def resolve_pub_info(self, info, **kwargs):
        return Pub.load()

class BreweryMutation(SerializerMutation):
    class Meta:
        serializer_class = BrewerySerializer

class Mutation(ObjectType):
    mutate_brewery = BreweryMutation.Field()             
                               
schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)
