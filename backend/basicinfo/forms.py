from django import forms
from django.db.models import Q

from .models import Network, Station
from instruments.models import InstrumentEntity


class NetworkForm(forms.ModelForm):
    code = forms.CharField(max_length=5, min_length=2, label="台网代码")

    class Meta:
        model = Network
        fields = [
            "code",
            "name",
            "remark",
        ]


class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = [
            "network",
            "code",
            "name",
            "latitude",
            "longitude",
            "altitude",
            "establish",
            "removal",
            "remark",
        ]


class StationAdminForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = "__all__"

    seismic_instruments = forms.ModelMultipleChoiceField(
        queryset=InstrumentEntity.objects.filter(status="in_warehouse")
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            # self.fields['seismic_instruments'].widget = forms.SelectMultiple()
            self.fields[
                "seismic_instruments"
            ].queryset = InstrumentEntity.objects.filter(
                Q(status="in_warehouse") | Q(by_used=self.instance)
            )
            self.fields[
                "seismic_instruments"
            ].initial = self.instance.seismic_instruments.all()

    def save(self, commit, *args, **kwargs):
        instance = super().save(commit=False)
        old_instruments = InstrumentEntity.objects.none()
        if self.fields["seismic_instruments"].initial:
            old_instruments = self.fields["seismic_instruments"].initial
            old_instruments.update(by_used=None, status="unknow")
        new_instruments = self.cleaned_data["seismic_instruments"]
        instance.seismic_instruments.add(*new_instruments)
        new_instruments.update(status="online")
        if commit:
            instance.save()

        return instance
