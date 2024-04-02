from django import forms
from .models import Contact,Blog,BlogComment
from ckeditor.widgets import CKEditorWidget


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your first Name', 'autocomplete': 'off'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your last Name', 'autocomplete': 'off'}),
            "e_mail": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your email', 'autocomplete': 'off'}),
            "phone_number": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your phone number', 'autocomplete': 'off'}),
            "contact_message": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your message', 'autocomplete': 'off'}),
        }

class CreateBlogForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
        exclude = ('post_date','slug')
        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id':'author', 'type':'hidden'}),
            'mini_description': forms.Textarea(attrs={'class': 'form-control'})
        }

class UpdateBlogForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
        exclude = ('post_date','slug')
        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id':'author', 'type':'hidden'}),
            'mini_description': forms.Textarea(attrs={'class': 'form-control'})
        }
    
class CommentBlogForm(forms.ModelForm):
    
    class Meta:
        model = BlogComment
        fields = '__all__'
        
        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id':'author', 'type':'hidden'}),
            'blog': forms.TextInput(attrs={'value': '', 'id':'blog', 'type':'hidden'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),

        }