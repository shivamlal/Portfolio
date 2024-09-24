from django import forms
from .models import Contact
from .models import Experience


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'mobile', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: jone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ex: abc@gmail.com'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 0000000000'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter your message'}),
        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'company', 'start_date', 'end_date', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }