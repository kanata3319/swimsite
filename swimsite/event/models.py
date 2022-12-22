from django.db import models

class SEX(models.TextChoices):
    MAN = 'man', '男子'
    WOMAN = 'women', '女子'


class RELAY_SEX(models.TextChoices):
    MAN = 'man', '男子'
    WOMAN = 'women', '女子'
    MIXED = 'mixed', '混合'


class Player(models.Model):
    class Meta:
        verbose_name = '選手'

    last_name = models.CharField(
        verbose_name='姓',
        max_length=10,
    )

    first_name = models.CharField(
        verbose_name='名',
        max_length=10,
    )

    sex = models.CharField(
        verbose_name = '性別',
        max_length=5,
        choices=SEX.choices,
    )

    birthday = models.DateField(
        verbose_name='生年月日',
    )

    def __str__(self):
        return self.last_name + ' ' + self.first_name


class Competition(models.Model):
    class Meta:
        verbose_name = '大会'

    name = models.CharField(
        verbose_name='大会名',
        max_length=256,
    )
    
    event_date = models.DateField(
        verbose_name='開催日',
    )

    def __str__(self):
        return self.name + '(' + str(self.event_date) + ')'


class IndividualEvent(models.Model):
    class Meta:
        verbose_name = '個人種目'

    class Style(models.TextChoices):
        FREE = 'free', '自由形'
        BREAST = 'breast', '平泳ぎ'
        BACK = 'back', '背泳ぎ'
        BUTTERFLY = 'butterfly', 'バタフライ'
        INDIVIDUAL_MEDLEY = 'individual medley', '個人メドレー'

    style = models.CharField(
        verbose_name = '泳法',
        max_length=17,
        choices=Style.choices,
    )

    class Distance(models.IntegerChoices):
        METER_25 = 25, '25m'
        METER_50 = 50, '50m'
        METER_100 = 100, '100m'
        METER_200 = 200, '200m'
        METER_400 = 400, '400m'
        METER_800 = 800, '800m'
        METER_1500 = 1500, '1500m'

    distance = models.SmallIntegerField(
        verbose_name = '距離',
        choices=Distance.choices,
    )

    sex = models.CharField(
        verbose_name = '性別',
        max_length=5,
        choices=SEX.choices,
    )

    def __str__(self):
        return self.get_sex_display() + self.get_distance_display() + self.get_style_display()


class IndividualEventResult(models.Model):
    class Meta:
        verbose_name = '個人種目結果'

    competition = models.ForeignKey(
        Competition,
        verbose_name = '大会',
        on_delete=models.CASCADE,
    )

    player = models.ForeignKey(
        Player,
        verbose_name = '泳者',
        on_delete=models.CASCADE,
    )

    event = models.ForeignKey(
        IndividualEvent,
        verbose_name = '種目',
        on_delete=models.CASCADE,
    )

    time = models.TimeField(
        verbose_name = '時間',
        null=True, blank=True,
    )

    all_rank = models.PositiveSmallIntegerField(
        verbose_name = '全体順位',
        null=True, blank=True,
    )

    class_rank = models.PositiveSmallIntegerField(
        verbose_name = 'クラス順位',
        null=True, blank=True,
    )


class RelayEvent(models.Model):
    class Meta:
        verbose_name = 'リレー種目'

    class Style(models.TextChoices):
        FREE_RELAY = 'free relay', 'フリーリレー'
        MEDLEY_RELAY = 'medley relay', 'メドレーリレー'

    style = models.CharField(
        verbose_name = '泳法',
        max_length=17,
        choices=Style.choices,
    )

    class Distance(models.IntegerChoices):
        METER_100 = 100, '100m'
        METER_200 = 200, '200m'
        METER_400 = 400, '400m'
        METER_800 = 800, '800m'

    distance = models.PositiveSmallIntegerField(
        verbose_name = '距離',
        choices=Distance.choices,
    )

    sex = models.CharField(
        verbose_name = '性別',
        max_length=5,
        choices=RELAY_SEX.choices,
    )


class RelayEventResult(models.Model):
    class Meta:
        verbose_name = 'リレー種目結果'

    competition = models.ForeignKey(
        Competition,
        verbose_name = '大会',
        on_delete=models.CASCADE,
    )

    event = models.ForeignKey(
        IndividualEvent,
        verbose_name = '種目',
        on_delete=models.CASCADE,
    )

    player_1 = models.ForeignKey(
        Player,
        verbose_name = '第1泳者',
        on_delete=models.CASCADE,
        related_name="player_1",
    )

    player_2 = models.ForeignKey(
        Player,
        verbose_name = '第2泳者',
        on_delete=models.CASCADE,
        related_name="player_2",
    )

    player_3 = models.ForeignKey(
        Player,
        verbose_name = '第3泳者',
        on_delete=models.CASCADE,
        related_name="player_3",
    )

    player_4 = models.ForeignKey(
        Player,
        verbose_name = '第4泳者',
        on_delete=models.CASCADE,
        related_name="player_4",
    )

    time = models.TimeField(
        verbose_name = '時間',
        null=True, blank=True,
    )

    all_rank = models.PositiveSmallIntegerField(
        verbose_name = '全体順位',
        null=True, blank=True,
    )

    class_rank = models.PositiveSmallIntegerField(
        verbose_name = 'クラス順位',
        null=True, blank=True,
    )
