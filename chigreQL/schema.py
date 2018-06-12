import graphene

from graphene import relay, ObjectType

from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from chigre.models import Brewery


class BreweryNode(DjangoObjectType):
    
    class Meta:
        model = Brewery
        filter_fields = {
            'name': ['exact','istartswith'],
            'description': ['exact','istartswith'],
            }
        interfaces = (relay.Node, )


class Query(ObjectType):

    breweries = relay.Node.Field(BreweryNode)
    all_breweries = DjangoFilterConnectionField(BreweryNode)

    def resolve_breweries(self):
        return Brewery.objects.all()

schema = graphene.Schema(query=Query,)