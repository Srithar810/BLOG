
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Your User Name',
        })
        
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Your Password',
        })
    class Meta:
        fields = ['username','password']

class SignupForm(UserCreationForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Your User Name',
        })
        
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Your first Name',
        })
        
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Your Last Name',
        })
        
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Your email',
        })
        
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Your Password',
        })
        
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Your Confirm Password',
        })
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =  ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your first Name', 'autocomplete': 'off'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your last Name', 'autocomplete': 'off'}),
        }

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Old password'}))
    new_password1 = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'New password'}))
    new_password2 = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm New password'}))
    
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

class EditUserProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Lastname'}))
    username = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Lastname'}))
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']