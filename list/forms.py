from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from list.models import ToDoModel

class ToDoForm(forms.ModelForm):
    class Meta:
        model=ToDoModel
        fields =['title','description','level']
        
class Signup_Form(UserCreationForm):
    password2=forms.CharField(label='Confirm Password:',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}

        
class TaskSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)
    
class TaskOrdering(forms.Form):
    ordering= forms.CharField(label='Sort', max_length=100)
    
class edit_profile_from(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}