from django import forms


#Creating Forms

class InputForm(forms.Form):
    hero_name = forms.CharField(max_length=50)
    alter_ego = forms.CharField(max_length=50)
    primary_ability = forms.CharField(max_length=50)
    secondary_ability = forms.CharField(max_length=50)
    catchphrase = forms.CharField(max_length=60)
