from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    # pass
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'password2',
        ]


class User_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

class Profile_form(forms.ModelForm):

    gend = [

        ("Male", "Male"),
        ("Female", "Female")
    ]

    profile_passport = forms.ImageField(required=False, label='Profile passport')
    means_of_identity = forms.ImageField(required=False, label='means_of_identity')
    particulars = forms.FileField(required=False, label='particulars')
    gender = forms.ChoiceField(choices=gend, required=True, widget=forms.RadioSelect)
    staff = forms.BooleanField(required=False, label='staff')

    class Meta:
        model = Profile
        fields = [

        'address',
        'phone',
        'date_of_birth',
        'gender',
        'nationality',
        'state',
        'means_of_identity',
        'particulars',
        'profile_passport',
        'position',
        'department',
        'marital_status',
        'next_of_kin',
        'staff',
        'status',
        
        ]

        widgets = {
            'date_of_birth': forms.NumberInput(attrs={'type': 'date'}),
        }
    
    
    

