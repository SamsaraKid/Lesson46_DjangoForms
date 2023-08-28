from django import forms


class NashaForma(forms.Form):
    name = forms.CharField(label='Имя')
    num = forms.IntegerField(label='Номер', required=False, max_value=100, initial=12, help_text='напишите число', disabled=True)


class Forma2(forms.Form):
    k1 = forms.DecimalField(label='десятичные числа')
    k2 = forms.EmailField(label='почта', )
    k3 = forms.BooleanField(label='поставьте галочку', required=False)
    k4 = forms.NullBooleanField(label='вы человек')
    k5 = forms.URLField(label='адрес сайта', help_text='http://www.e1.ru')
    k7 = forms.FilePathField(label='выберите файл', path='C:/Users/koany/OneDrive/Рабочий стол', allow_files=True)
    k8 = forms.ImageField(label='картинка')
    vibor = (('английский', 'En'), ('русский', 'Ru'), ('французский', 'Fr'))
    k10 = forms.TypedChoiceField(choices=vibor)


class Uploadforma(forms.Form):
    name = forms.CharField()
    img = forms.ImageField()
