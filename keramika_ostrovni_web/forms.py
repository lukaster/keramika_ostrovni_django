from django import forms

from .models import Krouzek, Dite, Dospely, KontaktInfo


class DiteForm(forms.ModelForm):
    class Meta:
        model = Dite
        fields = [
            'jmeno',
            'prijmeni',
            'rocnik',
            'paralelka',
            've_skolnim_roce'
        ]

class DospelyForm(forms.ModelForm):
    class Meta:
        model = Dospely
        fields = [
            'jmeno',
            'prijmeni'
        ]

class KontaktInfoForm(forms.ModelForm):
    class Meta:
        model = KontaktInfo
        fields = [
            'jmeno',
            'prijmeni',
            'telefoni_cislo',
            'email'
        ]
