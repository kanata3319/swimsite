import datetime
from decimal import Decimal
import pytz
from django.conf import settings
# from django.utils.timezone import localtime
from event import models as e_models
from event import factories as e_fac

tz = pytz.timezone(settings.TIME_ZONE)


def run():
    '''
    Usage:
        python namage.py runscript load_mst_data
    '''
    # Player
    tanaka = e_fac.PlayerFactory(
        last_name='田中',
        first_name='翔太',
        sex=e_models.SEX.MAN,
        birthday=tz.localize(datetime.datetime(1992, 4, 1))
    )
    yoshi = e_fac.PlayerFactory(
        last_name='吉',
        first_name='順',
        sex=e_models.SEX.MAN,
        birthday=tz.localize(datetime.datetime(1992, 4, 1))
    )
    huku = e_fac.PlayerFactory(
        last_name='福',
        first_name='圭',
        sex=e_models.SEX.MAN,
        birthday=tz.localize(datetime.datetime(1992, 4, 1))
    )

    # 個人競技
    # Free
    m_25_free = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_25,
        sex=e_models.SEX.MAN
    )
    w_25_free = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_25,
        sex=e_models.SEX.WOMAN
    )
    m_50_free = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_50,
        sex=e_models.SEX.MAN
    )
    w_50_free = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_50,
        sex=e_models.SEX.WOMAN
    )
    m_100_free = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.MAN
    )
    w_100_free = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.WOMAN
    )
    m_200_free = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.MAN
    )
    w_200_free = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.WOMAN
    )
    m_400_free = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_400,
        sex=e_models.SEX.MAN
    )
    w_400_free = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.FREE,
        distance=e_models.IndividualEvent.Distance.METER_400,
        sex=e_models.SEX.WOMAN
    )
    # Breast
    m_25_breast = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BREAST,
        distance=e_models.IndividualEvent.Distance.METER_25,
        sex=e_models.SEX.MAN
    )
    w_25_breast = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BREAST,
        distance=e_models.IndividualEvent.Distance.METER_25,
        sex=e_models.SEX.WOMAN
    )
    m_50_breast = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BREAST,
        distance=e_models.IndividualEvent.Distance.METER_50,
        sex=e_models.SEX.MAN
    )
    w_50_breast = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BREAST,
        distance=e_models.IndividualEvent.Distance.METER_50,
        sex=e_models.SEX.WOMAN
    )
    m_100_breast = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BREAST,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.MAN
    )
    w_100_breast = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BREAST,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.WOMAN
    )
    m_200_breast = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BREAST,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.MAN
    )
    w_200_breast = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BREAST,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.WOMAN
    )
    # Back
    m_25_back = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BACK,
        distance=e_models.IndividualEvent.Distance.METER_25,
        sex=e_models.SEX.MAN
    )
    w_25_back = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BACK,
        distance=e_models.IndividualEvent.Distance.METER_25,
        sex=e_models.SEX.WOMAN
    )
    m_50_back = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BACK,
        distance=e_models.IndividualEvent.Distance.METER_50,
        sex=e_models.SEX.MAN
    )
    w_50_back = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BACK,
        distance=e_models.IndividualEvent.Distance.METER_50,
        sex=e_models.SEX.WOMAN
    )
    m_100_back = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BACK,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.MAN
    )
    w_100_back = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BACK,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.WOMAN
    )
    m_200_back = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BACK,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.MAN
    )
    w_200_back = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BACK,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.WOMAN
    )
    # Butterfly
    m_25_butterfly = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BUTTERFLY,
        distance=e_models.IndividualEvent.Distance.METER_25,
        sex=e_models.SEX.MAN
    )
    w_25_butterfly = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BUTTERFLY,
        distance=e_models.IndividualEvent.Distance.METER_25,
        sex=e_models.SEX.WOMAN
    )
    m_50_butterfly = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BUTTERFLY,
        distance=e_models.IndividualEvent.Distance.METER_50,
        sex=e_models.SEX.MAN
    )
    w_50_butterfly = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BUTTERFLY,
        distance=e_models.IndividualEvent.Distance.METER_50,
        sex=e_models.SEX.WOMAN
    )
    m_100_butterfly = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BUTTERFLY,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.MAN
    )
    w_100_butterfly = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BUTTERFLY,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.WOMAN
    )
    m_200_butterfly = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BUTTERFLY,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.MAN
    )
    w_200_butterfly = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.BUTTERFLY,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.WOMAN
    )
    # Medley
    m_100_ind_medley = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.INDIVIDUAL_MEDLEY,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.MAN
    )
    w_100_ind_medley = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.INDIVIDUAL_MEDLEY,
        distance=e_models.IndividualEvent.Distance.METER_100,
        sex=e_models.SEX.WOMAN
    )
    m_200_ind_medley = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.INDIVIDUAL_MEDLEY,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.MAN
    )
    w_200_ind_medley = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.INDIVIDUAL_MEDLEY,
        distance=e_models.IndividualEvent.Distance.METER_200,
        sex=e_models.SEX.WOMAN
    )
    m_400_ind_medley = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.INDIVIDUAL_MEDLEY,
        distance=e_models.IndividualEvent.Distance.METER_400,
        sex=e_models.SEX.MAN
    )
    w_400_ind_medley = e_fac.IndividualEventFactory(
        style=e_models.IndividualEvent.Style.INDIVIDUAL_MEDLEY,
        distance=e_models.IndividualEvent.Distance.METER_400,
        sex=e_models.SEX.WOMAN
    )

    # リレー競技
    # Free
    m_100_free_relay = e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.FREE_RELAY,
        distance=e_models.RelayEvent.Distance.METER_100,
        sex=e_models.RELAY_SEX.MAN
    )
    w_100_free_relay = e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.FREE_RELAY,
        distance=e_models.RelayEvent.Distance.METER_100,
        sex=e_models.RELAY_SEX.WOMAN
    )
    mix_100_free_relay = e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.FREE_RELAY,
        distance=e_models.RelayEvent.Distance.METER_100,
        sex=e_models.RELAY_SEX.MIXED
    )
    m_200_free_relay = e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.FREE_RELAY,
        distance=e_models.RelayEvent.Distance.METER_200,
        sex=e_models.RELAY_SEX.MAN
    )
    w_200_free_relay = e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.FREE_RELAY,
        distance=e_models.RelayEvent.Distance.METER_200,
        sex=e_models.RELAY_SEX.WOMAN
    )
    mix_200_free_relay = e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.FREE_RELAY,
        distance=e_models.RelayEvent.Distance.METER_200,
        sex=e_models.RELAY_SEX.MIXED
    )
    m_400_free_relay = e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.FREE_RELAY,
        distance=e_models.RelayEvent.Distance.METER_400,
        sex=e_models.RELAY_SEX.MAN
    )
    w_400_free_relay = e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.FREE_RELAY,
        distance=e_models.RelayEvent.Distance.METER_400,
        sex=e_models.RELAY_SEX.WOMAN
    )
    mix_400_free_relay = e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.FREE_RELAY,
        distance=e_models.RelayEvent.Distance.METER_400,
        sex=e_models.RELAY_SEX.MIXED
    )
    # Medley
    m_100_medley_relay = e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.MEDLEY_RELAY,
        distance=e_models.RelayEvent.Distance.METER_100,
        sex=e_models.RELAY_SEX.MAN
    )
    w_100_medley_relay = e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.MEDLEY_RELAY,
        distance=e_models.RelayEvent.Distance.METER_100,
        sex=e_models.RELAY_SEX.WOMAN
    )
    mix_100_medley_relay = e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.MEDLEY_RELAY,
        distance=e_models.RelayEvent.Distance.METER_100,
        sex=e_models.RELAY_SEX.MIXED
    )
    m_200_medley_relay = e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.MEDLEY_RELAY,
        distance=e_models.RelayEvent.Distance.METER_200,
        sex=e_models.RELAY_SEX.MAN
    )
    w_200_medley_relay = e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.MEDLEY_RELAY,
        distance=e_models.RelayEvent.Distance.METER_200,
        sex=e_models.RELAY_SEX.WOMAN
    )
    mix_200_medley_relay = e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.MEDLEY_RELAY,
        distance=e_models.RelayEvent.Distance.METER_200,
        sex=e_models.RELAY_SEX.MIXED
    )
    m_400_medley_relay = e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.MEDLEY_RELAY,
        distance=e_models.RelayEvent.Distance.METER_400,
        sex=e_models.RELAY_SEX.MAN
    )
    w_400_medley_relay = e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.MEDLEY_RELAY,
        distance=e_models.RelayEvent.Distance.METER_400,
        sex=e_models.RELAY_SEX.WOMAN
    )
    mix_400_medley_relay = e_fac.RelayEventFactory(
        style=e_models.RelayEvent.Style.MEDLEY_RELAY,
        distance=e_models.RelayEvent.Distance.METER_400,
        sex=e_models.RELAY_SEX.MIXED
    )
    # 大会
    competition_66 = e_fac.CompetitionFactory(
        name='第66回熊本マスターズ水泳競技大会',
        event_date=tz.localize(datetime.datetime(2017, 6, 18))
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_66,
        player=yoshi,
        event=m_50_free,
        time=Decimal('25.86'),
        all_rank=3,
        class_rank=10,
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_66,
        player=huku,
        event=m_25_butterfly,
        time=Decimal('12.48'),
        all_rank=1,
        class_rank=1,
    )
    e_fac.RelayEventResultFactory(
        competition=competition_66,
        event=m_100_free_relay,
        player_1=huku,
        player_4=yoshi,
        time=Decimal('46.79'),
        all_rank=1,
        class_rank=1,
    )
    e_fac.RelayEventResultFactory(
        competition=competition_66,
        event=m_100_medley_relay,
        player_2=yoshi,
        player_3=huku,
        time=Decimal('53.60'),
        all_rank=1,
        class_rank=1,
    )
    e_fac.RelayEventResultFactory(
        competition=competition_66,
        event=m_200_free_relay,
        player_3=huku,
        player_4=yoshi,
        time=Decimal('103.45'),
        all_rank=2,
        class_rank=2,
    )
    competition_67 = e_fac.CompetitionFactory(
        name='第67回熊本マスターズ水泳競技大会',
        event_date=tz.localize(datetime.datetime(2017, 11, 12))
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_67,
        player=tanaka,
        event=m_25_free,
        time=Decimal('13.97'),
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_67,
        player=yoshi,
        event=m_50_free,
        time=Decimal('25.17'),
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_67,
        player=yoshi,
        event=m_25_back,
        time=Decimal('14.80'),
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_67,
        player=huku,
        event=m_50_butterfly,
        time=Decimal('27.83'),
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_67,
        player=huku,
        event=m_25_butterfly,
        time=Decimal('12.90'),
    )
    e_fac.RelayEventResultFactory(
        competition=competition_67,
        event=m_200_medley_relay,
        player_2=tanaka,
        player_3=huku,
        time=Decimal('127.66'),
    )
    e_fac.RelayEventResultFactory(
        competition=competition_67,
        event=mix_100_medley_relay,
        player_2=tanaka,
        time=Decimal('67.12'),
    )
    e_fac.RelayEventResultFactory(
        competition=competition_67,
        event=m_100_medley_relay,
        player_2=tanaka,
        player_3=huku,
        time=Decimal('61.39'),
    )
    e_fac.RelayEventResultFactory(
        competition=competition_67,
        event=m_200_free_relay,
        player_1=huku,
        player_4=yoshi,
        time=Decimal('102.79'),
    )
    e_fac.RelayEventResultFactory(
        competition=competition_67,
        event=m_100_free_relay,
        player_4=yoshi,
        time=Decimal('46.93'),
    )
    competition_68 = e_fac.CompetitionFactory(
        name='第68回熊本マスターズ水泳競技大会',
        event_date=tz.localize(datetime.datetime(2018, 6, 17))
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_68,
        player=tanaka,
        event=m_25_free,
        time=Decimal('13.94'),
        all_rank=17,
        class_rank=2,
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_68,
        player=tanaka,
        event=m_25_breast,
        time=Decimal('17.25'),
        all_rank=7,
        class_rank=2,
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_68,
        player=yoshi,
        event=m_50_free,
        time=Decimal('25.39'),
        all_rank=3,
        class_rank=3,
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_68,
        player=huku,
        event=m_50_butterfly,
        time=Decimal('28.87'),
        all_rank=4,
        class_rank=1,
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_68,
        player=huku,
        event=m_25_butterfly,
        time=Decimal('13.21'),
        all_rank=1,
        class_rank=1,
    )
    # リレー未登録

    competition_69 = e_fac.CompetitionFactory(
        name='第69回熊本マスターズ水泳競技大会',
        event_date=tz.localize(datetime.datetime(2018, 11, 11))
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_69,
        player=tanaka,
        event=m_25_free,
        time=Decimal('13.67'),
        all_rank=26,
        class_rank=5,
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_69,
        player=tanaka,
        event=m_25_breast,
        time=Decimal('16.74'),
        all_rank=7,
        class_rank=2,
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_69,
        player=yoshi,
        event=m_50_butterfly,
        time=Decimal('27.26'),
        all_rank=6,
        class_rank=4,
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_69,
        player=yoshi,
        event=m_100_ind_medley,
        time=Decimal('65.23'),
        all_rank=4,
        class_rank=1,
    )
    # リレー未登録

    competition_70 = e_fac.CompetitionFactory(
        name='第70回熊本マスターズ水泳競技大会',
        event_date=tz.localize(datetime.datetime(2019, 6, 16))
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_70,
        player=tanaka,
        event=m_25_free,
        time=Decimal('13.67'),
        all_rank=17,
        class_rank=4,
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_70,
        player=tanaka,
        event=m_25_breast,
        time=Decimal('16.57'),
        all_rank=6,
        class_rank=1,
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_70,
        player=yoshi,
        event=m_50_breast,
        time=Decimal('34.09'),
        all_rank=4,
        class_rank=1,
    )
    # リレー未登録

    competition_71 = e_fac.CompetitionFactory(
        name='第71回熊本マスターズ水泳競技大会',
        event_date=tz.localize(datetime.datetime(2019, 11, 10))
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_71,
        player=tanaka,
        event=m_100_breast,
        time=Decimal('83.07'),
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_71,
        player=tanaka,
        event=m_25_free,
        time=Decimal('13.66'),
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_71,
        player=yoshi,
        event=m_100_breast,
        time=Decimal('74.87'),
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_71,
        player=yoshi,
        event=m_25_breast,
        time=Decimal('15.27'),
    )
    e_fac.IndividualEventResultFactory(
        competition=competition_71,
        player=huku,
        event=m_25_butterfly,
        time=Decimal('13.16'),
    )
    # リレー未登録
    competition_72 = e_fac.CompetitionFactory(
        name='第72回熊本マスターズ水泳競技大会(中止)',
        event_date=tz.localize(datetime.datetime(2021, 6, 1))
    )
