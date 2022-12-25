import factory
from event import models as e_models


class CompetitionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = e_models.Competition
        

class IndividualEventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = e_models.IndividualEvent


class RelayEventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = e_models.RelayEvent
