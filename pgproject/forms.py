from django import forms
from .models import PG
from .models import PGImage
from .models import Registrations
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class PgModelform(forms.ModelForm):
    class Meta:
        model = PG
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = PGImage
        fields = '__all__'

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registrations
        fields = '__all__'

class RegisterUser(UserCreationForm):
    class Meta:
        model= User
        fields = ['username','first_name','last_name','email','password1','password2']


class registeruser(UserCreationForm):
    class Meta:
        model= User
        fields = ['username','first_name','last_name','email','password1','password2']