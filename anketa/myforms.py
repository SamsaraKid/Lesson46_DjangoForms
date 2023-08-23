from django import forms

class NashaForma(forms.Form):
    name = forms.CharField(label='Имя')
    num = forms.IntegerField(label='Номер', required=False, max_value=100, initial=12, help_text='напишите число', disabled=True)