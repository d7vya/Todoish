from django import forms
from home.models import *


class UserTaskForm(forms.ModelForm):
    class Meta:
        model=Tasks
        fields=['title','desc','start_date','end_date','mark_important','status']
        widgets={'start_date':forms.DateInput(attrs={'type': 'date'}),
                 'end_date':forms.DateInput(attrs={'type': 'date'})}
class TeamTaskForm(forms.ModelForm):
    class Meta:
        model=Tasks
        fields=['title','desc','start_date','end_date','mark_important','assigned_to','status']   
        widgets={'start_date':forms.DateInput(attrs={'type': 'date'}),
                 'end_date':forms.DateInput(attrs={'type': 'date'})}
class TeamForm(forms.Form):
    name=forms.CharField(max_length=50,required=True)

        
