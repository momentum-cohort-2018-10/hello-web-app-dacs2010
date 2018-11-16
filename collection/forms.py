from django import forms
from collection.models import Thing


class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ('name', 'description',)
