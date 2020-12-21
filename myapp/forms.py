from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CompanyDetail

class SignupForm(UserCreationForm):
    Contact = forms.IntegerField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name' , 'last_name' , 'email','Contact']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = CompanyDetail
        fields = '__all__'