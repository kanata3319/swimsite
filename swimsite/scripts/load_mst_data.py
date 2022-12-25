from event import models as e_models
from event import factories as e_fac

def run():
    '''
    Usage:
        python namage.py runscript load_mst_data
    '''
    # 個人競技
    # Free
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_25,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_25,
        sex=e_models.SEX.WOMAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_50,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_50,
        sex=e_models.SEX.WOMAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.WOMAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.WOMAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_400,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_400,
        sex=e_models.SEX.WOMAN
    )
    # Breast
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BREAST,
        distance=e_models.IndividualEvent.Distance.METER_25,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BREAST,
        distance=e_models.IndividualEvent.Distance.METER_25,
        sex=e_models.SEX.WOMAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BREAST,
        distance=e_models.IndividualEvent.Distance.METER_50,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BREAST,
        distance=e_models.IndividualEvent.Distance.METER_50,
        sex=e_models.SEX.WOMAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BREAST,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BREAST,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.WOMAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BREAST,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BREAST,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.WOMAN
    )
    # Back
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BACK,
        distance=e_models.IndividualEvent.Distance.METER_25,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BACK,
        distance=e_models.IndividualEvent.Distance.METER_25,
        sex=e_models.SEX.WOMAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BACK,
        distance=e_models.IndividualEvent.Distance.METER_50,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BACK,
        distance=e_models.IndividualEvent.Distance.METER_50,
        sex=e_models.SEX.WOMAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BACK,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BACK,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.WOMAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BACK,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BACK,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.WOMAN
    )
    # Butterfly
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BUTTERFLY,
        distance=e_models.IndividualEvent.Distance.METER_25,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BUTTERFLY,
        distance=e_models.IndividualEvent.Distance.METER_25,
        sex=e_models.SEX.WOMAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BUTTERFLY,
        distance=e_models.IndividualEvent.Distance.METER_50,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BUTTERFLY,
        distance=e_models.IndividualEvent.Distance.METER_50,
        sex=e_models.SEX.WOMAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BUTTERFLY,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BUTTERFLY,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.WOMAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BUTTERFLY,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BUTTERFLY,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.WOMAN
    )
    # Medley
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.INDIVIDUAL_MEDLEY,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.INDIVIDUAL_MEDLEY,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.WOMAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.INDIVIDUAL_MEDLEY,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.INDIVIDUAL_MEDLEY,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.WOMAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.INDIVIDUAL_MEDLEY,
        distance=e_models.IndividualEvent.Distance.METER_400,
        sex=e_models.SEX.MAN
    )
    e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.INDIVIDUAL_MEDLEY,
        distance=e_models.IndividualEvent.Distance.METER_400,
        sex=e_models.SEX.WOMAN
    )

    # リレー競技
    # Free
    e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.FREE_RELAY,
        distance=e_models.RelayEvent.Distance.METER_100,
        sex=e_models.RELAY_SEX.MAN
    )
    e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.FREE_RELAY,
        distance=e_models.RelayEvent.Distance.METER_100,
        sex=e_models.RELAY_SEX.WOMAN
    )
    e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.FREE_RELAY,
        distance=e_models.RelayEvent.Distance.METER_100,
        sex=e_models.RELAY_SEX.MIXED
    )
    e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.FREE_RELAY,
        distance=e_models.RelayEvent.Distance.METER_200,
        sex=e_models.RELAY_SEX.MAN
    )
    e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.FREE_RELAY,
        distance=e_models.RelayEvent.Distance.METER_200,
        sex=e_models.RELAY_SEX.WOMAN
    )
    e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.FREE_RELAY,
        distance=e_models.RelayEvent.Distance.METER_200,
        sex=e_models.RELAY_SEX.MIXED
    )
    e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.FREE_RELAY,
        distance=e_models.RelayEvent.Distance.METER_400,
        sex=e_models.RELAY_SEX.MAN
    )
    e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.FREE_RELAY,
        distance=e_models.RelayEvent.Distance.METER_400,
        sex=e_models.RELAY_SEX.WOMAN
    )
    e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.FREE_RELAY,
        distance=e_models.RelayEvent.Distance.METER_400,
        sex=e_models.RELAY_SEX.MIXED
    )
    # Medley
    e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.MEDLEY_RELAY,
        distance=e_models.RelayEvent.Distance.METER_100,
        sex=e_models.RELAY_SEX.MAN
    )
    e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.MEDLEY_RELAY,
        distance=e_models.RelayEvent.Distance.METER_100,
        sex=e_models.RELAY_SEX.WOMAN
    )
    e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.MEDLEY_RELAY,
        distance=e_models.RelayEvent.Distance.METER_100,
        sex=e_models.RELAY_SEX.MIXED
    )
    e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.MEDLEY_RELAY,
        distance=e_models.RelayEvent.Distance.METER_200,
        sex=e_models.RELAY_SEX.MAN
    )
    e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.MEDLEY_RELAY,
        distance=e_models.RelayEvent.Distance.METER_200,
        sex=e_models.RELAY_SEX.WOMAN
    )
    e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.MEDLEY_RELAY,
        distance=e_models.RelayEvent.Distance.METER_200,
        sex=e_models.RELAY_SEX.MIXED
    )
    e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.MEDLEY_RELAY,
        distance=e_models.RelayEvent.Distance.METER_400,
        sex=e_models.RELAY_SEX.MAN
    )
    e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.MEDLEY_RELAY,
        distance=e_models.RelayEvent.Distance.METER_400,
        sex=e_models.RELAY_SEX.WOMAN
    )
    e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.MEDLEY_RELAY,
        distance=e_models.RelayEvent.Distance.METER_400,
        sex=e_models.RELAY_SEX.MIXED
    )