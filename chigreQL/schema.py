import graphene

from graphene import Node, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation

from chigre.models import Brewery, BeerType, KegType, Beer, Keg, TapType, Tap
from chigre.serializers import BrewerySerializer

class BreweryNode(DjangoObjectType):
    class Meta:
        model = Brewery
        exclude_fields = ('created')
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'description': ['istartswith', 'icontains'],
            'country': ['exact'],
            }
        interfaces = (Node, )

class BeerTypeNode(DjangoObjectType):
    class Meta:
        model = BeerType
        exclude_fields = ('created')
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
        exclude_fields = ('created')
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'description': ['istartswith', 'icontains'],
            }
        interfaces = (Node, )

class KegNode(DjangoObjectType):
    class Meta:
        model = Keg
        exclude_fields = ('created')
        filter_fields = {
            }
        interfaces = (Node, )

class TapNode(DjangoObjectType):
    class Meta:
        model = Tap
        exclude_fields = ('created')
        filter_fields = {
            'number': ['exact'],
            }
        interfaces = (Node, )

class Query(ObjectType):
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

class BreweryMutation(SerializerMutation):
    class Meta:
        serializer_class = BrewerySerializer

class Mutation(ObjectType):
    mutate_brewery = BreweryMutation.Field()
    model_operations = ['create', 'update']
    lookup_field = 'id'

    @classmethod
    def get_serializer_kwargs(cls, root, info, **input):
        if 'id' in input:
            instance = Post.objects.filter(id=input['id']).first()
            if instance:
                return {'instance': instance, 'data': input, 'partial': True}
            else:
                raise http.Http404
        return {'data': input, 'partial': True}                               
                               
schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)
