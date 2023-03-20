from django import forms
from event import models as e_models


class RecordKojinForm(forms.Form):
    player = forms.ModelChoiceField(
        e_models.Player.objects.all(),
        label="選手名"
    )

    competition = forms.ModelChoiceField(
        e_models.Competition.objects.all(),
        label="大会名",
        required=False,
        empty_label='ALL',
    )

    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs["class"] = "form-control"
        super().__init__(*args, **kwargs)


class RecordTaikaiForm(forms.Form):
    competition = forms.ModelChoiceField(
        e_models.Competition.objects.all(),
        label="大会名",
    )

    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs["class"] = "form-control"
        super().__init__(*args, **kwargs)


class RecordCreateKojinForm(forms.ModelForm):
    class Meta:
        model = e_models.IndividualEventResult
        exclude = ('time', )

    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs["class"] = "form-control"
        super().__init__(*args, **kwargs)

    time_minute = forms.DecimalField(
        label="タイム(分)",
        initial=0,
        min_value=0,
    )

    time_second = forms.DecimalField(
        label="タイム(秒)",
        initial=0,
        min_value=0,
    )

    time_mili_second = forms.DecimalField(
        label="タイム(ミリ秒)",
        initial=0,
        max_value=99,
        min_value=0,
    )
