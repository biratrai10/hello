from django import forms
from .models import ContactInfo


class ContactInfoForm(forms.ModelForm):

    class Meta:
        model = ContactInfo
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'name':'dzother[Name]','id':'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address', 'name': 'dzother[Email]','id':'email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone', 'name': 'dzother[Phone]','id':'phone'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject', 'name': 'dzother[Subject]','id':'subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message..', 'rows':'4' , 'name': 'message','id':'message'}),
        }