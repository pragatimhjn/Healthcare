from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Userinfo 


class staffdata(forms.Form):
    
    name=forms.CharField(max_length=100)
    sid=forms.IntegerField()
    dept=forms.CharField(max_length=100)
    promotion=forms.BooleanField()
    phonenum=forms.IntegerField()
    email=forms.EmailField()

class MyUserCreationForm(UserCreationForm):
    # whatyouare = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect())

    class Meta(UserCreationForm):
        model = Userinfo 
        fields = ('username','email','is_doctor', 'is_patient')


