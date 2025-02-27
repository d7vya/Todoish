from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields= ['username','email','first_name','last_name','password']
        help_texts={'username':None}
        widgets={
            'password':forms.PasswordInput()
        }
class LoginForm(forms.Form):
    username=forms.CharField( max_length=100, required=True)
    password=forms.CharField(widget=forms.PasswordInput(), required=True)