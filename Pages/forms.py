from django import forms
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Adınızı Giriniz',
    }))
    last_name=forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Soyadınızı Giriniz',
    }))
    email=forms.EmailField(
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder':'adsoyad@gmail.com',
    }))
    phone=forms.CharField(
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder':'(---) --- -- --',
    }))
    message=forms.CharField(
        widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder':'Mesajınızı Yazınız...',
    })
    )
    
    class Meta:
        model = Contact
        fields = ['first_name','last_name','email','phone','message']
    