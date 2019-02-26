from django import forms
from . models import users
class Form(forms.Form):
    ans = forms.CharField(label="ans",max_length=50)

class submit_form(forms.Form):
    name = forms.CharField(label="name", max_length=50)
    team_id = forms.IntegerField(label="id")