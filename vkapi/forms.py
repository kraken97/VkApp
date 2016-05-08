from django.forms import ModelForm
from django import  forms

class TokenConfirm(forms.Form):
    token=forms.Field(required=True)


class Message(forms.Form):
    msg=forms.Field(required=True)
