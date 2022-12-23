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
