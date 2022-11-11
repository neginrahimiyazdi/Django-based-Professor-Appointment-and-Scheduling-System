from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length=50)
    student_number = forms.IntegerField()
    
#size = fields.IntegerRangeField(min_value=-100, max_value=100)

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','student_number','email', 'password1', 'password2']
