import factory
from event import models as e_models


class PlayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = e_models.Player


class CompetitionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = e_models.Competition


class IndividualEventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = e_models.IndividualEvent


class IndividualEventResultFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = e_models.IndividualEventResult


class RelayEventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = e_models.RelayEvent


class RelayEventResultFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = e_models.RelayEventResult
