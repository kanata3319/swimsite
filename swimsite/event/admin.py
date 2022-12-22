from django.contrib import admin
from event import models as e_models


@admin.register(e_models.Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', ]


@admin.register(e_models.Competition)
class CompetitionAdmin(admin.ModelAdmin):
    pass


@admin.register(e_models.IndividualEvent)
class IndividualEventAdmin(admin.ModelAdmin):
    pass


@admin.register(e_models.IndividualEventResult)
class IndividualEventResultAdmin(admin.ModelAdmin):
    pass


@admin.register(e_models.RelayEvent)
class RelayEventAdmin(admin.ModelAdmin):
    pass


@admin.register(e_models.RelayEventResult)
class RelayEventResultAdmin(admin.ModelAdmin):
    pass
