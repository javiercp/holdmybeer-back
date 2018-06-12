import graphene

from graphene import relay, ObjectType

from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from chigre.models import Brewery, BeerType, KegType, Beer, Keg, TapType, Tap


class BreweryNode(DjangoObjectType):

    class Meta:
        model = Brewery
        filter_fields = {
            'name': ['exact','istartswith'],
            'description': ['exact','istartswith'],
            'country': ['exact','istartswith'],
            }
        interfaces = (relay.Node, )

class BeerTypeNode(DjangoObjectType):

    class Meta:
        model = BeerType
        filter_fields = {
            'name': ['exact','istartswith'],
            'description': ['exact','istartswith'],
            }
        interfaces = (relay.Node, )

class KegTypeNode(DjangoObjectType):
    
    class Meta:
        model = KegType
        filter_fields = {
            'name': ['exact','istartswith'],
            'size': ['exact'],
            }
        interfaces = (relay.Node, )

class BeerNode(DjangoObjectType):

    class Meta:
        model = Beer
        filter_fields = {
            'name': ['exact','istartswith'],
            'description': ['exact','istartswith'],
            }
        interfaces = (relay.Node, )

class KegNode(DjangoObjectType):

    class Meta:
        model = Keg
        filter_fields = {
            }
        interfaces = (relay.Node, )

class TapTypeNode(DjangoObjectType):
    
    class Meta:
        model = TapType
        filter_fields = {
            'name': ['exact','istartswith'],
            }
        interfaces = (relay.Node, )

class TapNode(DjangoObjectType):
    
    class Meta:
        model = Tap
        filter_fields = {
            'number': ['exact'],
            }
        interfaces = (relay.Node, )

class Query(ObjectType):

    breweries = relay.Node.Field(BreweryNode)
    all_breweries = DjangoFilterConnectionField(BreweryNode)
    beertypes = relay.Node.Field(BeerTypeNode)
    all_beertypes = DjangoFilterConnectionField(BeerTypeNode)
    kegtypes = relay.Node.Field(KegTypeNode)
    all_kegtypes = DjangoFilterConnectionField(KegTypeNode)
    beers = relay.Node.Field(BeerNode)
    all_beers = DjangoFilterConnectionField(BeerNode)
    kegs = relay.Node.Field(KegNode)
    all_kegs = DjangoFilterConnectionField(KegNode)
    taptypes = relay.Node.Field(TapTypeNode)
    all_taptypes = DjangoFilterConnectionField(TapTypeNode)
    taps = relay.Node.Field(TapNode)
    all_taps = DjangoFilterConnectionField(TapNode)

    def resolve_breweries(self):
        return Brewery.objects.all()

    def resolve_beertypes(self):
        return BeerType.objects.all()

    def resolve_kegtypes(self):
        return KegType.objects.all()

    def resolve_beers(self):
        return Beer.objects.all()

    def resolve_kegs(self):
        return Keg.objects.all()

    def resolve_taptypes(self):
        return TapType.objects.all()

    def resolve_taps(self):
        return Tap.objects.all()

schema = graphene.Schema(query=Query,)