

from django import forms
from .model import User

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class LoginForm(forms.Form):
    user = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput())

class ParametersForm(forms.Form) :
    pdie = forms.CharField(max_length=10,label="Protein dielectric constant", required=False)
    saltconc = forms.CharField(max_length=10, label="Salt concentration",required=False)
    ligand = forms.CharField(max_length=10, label="Ligand name")
    charges = forms.CharField(max_length=10, label="Ligand net charge", required=False)
    #submit = forms.su
    #docfile = forms.FileField(label='Select a file')

class UserForm(forms.ModelForm):
    class Meta:
        model = User # Your User model
        fields = '__all__'
