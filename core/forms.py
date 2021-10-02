from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select, CheckboxInput
from django.utils.translation import gettext_lazy as _
from .models import Startup, Investor, Contact

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class StartupModelForm(ModelForm):
    class Meta:
        model = Startup
        fields = '__all__'
        exclude = ['slug','status']
        labels = {
            'motivation': _('Reason for applying'),
        }
        widgets = {
            'name': TextInput(attrs={'placeholder': 'e.g. Koko Energies', 'class': 'form-control'}),
            'web_address': TextInput(attrs={'class': 'form-control'}),
            'startup_pitch': Textarea(attrs={'cols': 10, 'rows': 3, 'class': 'form-control'}),
            'startup_stage': Select(attrs={'class': 'form-control'}),
            'start_month': Select(attrs={'class': 'form-control', 'placeholder': 'Month'}),
            'start_year': Select(attrs={'class': 'form-control', 'placeholder': 'Year'}),
            # 'incorporation': CheckboxInput(attrs={'class': 'form-control'}),
            'country': TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'city': TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'applicant_title': TextInput(attrs={'placeholder': 'e.g. Chief Exective Officer', 'class': 'form-control'}),
            'applicant_role': Select(attrs={'class': 'form-control'}),
            'applicant_first_name': TextInput(attrs={'class': 'form-control'}),
            'applicant_last_name': TextInput(attrs={'class': 'form-control'}),
            'applicant_email': TextInput(attrs={'class': 'form-control'}),
            'applicant_phone_no': TextInput(attrs={'class': 'form-control'}),
            'linkedin_account': TextInput(attrs={'placeholder': 'https://www.linkedin.com/in/..', 'class': 'form-control'}),
            'applicant_bio': Textarea(attrs={'cols': 10, 'rows': 3, 'placeholder': 'Describe yourself in 300 words', 'class': 'form-control'}),
            'startup_elevator_pitch': Textarea(attrs={'cols': 10, 'rows': 3, 'placeholder': 'Write in not more than 300 words', 'class': 'form-control'}),
            'motivation': Textarea(attrs={'cols': 10, 'rows': 3, 'class': 'form-control'}),
        }


class StartupEditForm(ModelForm):
    class Meta:
        model = Startup
        fields = '__all__'
        exclude = ['slug']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'web_address': TextInput(attrs={'class': 'form-control'}),
            'startup_pitch': Textarea(attrs={'cols': 10, 'rows': 3, 'class': 'form-control'}),
            'startup_stage': Select(attrs={'class': 'form-control'}),
            'start_month': Select(attrs={'class': 'form-control'}),
            'start_year': Select(attrs={'class': 'form-control'}),
            # 'incorporation': CheckboxInput(attrs={'class': 'form-control'}),
            'country': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'applicant_title': TextInput(attrs={'class': 'form-control'}),
            'applicant_role': Select(attrs={'class': 'form-control'}),
            'applicant_first_name': TextInput(attrs={'class': 'form-control'}),
            'applicant_last_name': TextInput(attrs={'class': 'form-control'}),
            'applicant_email': TextInput(attrs={'class': 'form-control'}),
            'applicant_phone_no': TextInput(attrs={'class': 'form-control'}),
            'linkedin_account': TextInput(attrs={'class': 'form-control'}),
            'applicant_bio': Textarea(attrs={'cols': 10, 'rows': 3, 'class': 'form-control'}),
            'startup_elevator_pitch': Textarea(attrs={'cols': 10, 'rows': 3, 'class': 'form-control'}),
            'motivation': Textarea(attrs={'cols': 10, 'rows': 3, 'class': 'form-control'}),
            'status': Select(attrs={'class': 'form-control'})
        }


class InvestorModelForm(ModelForm):
    class Meta:
        model = Investor
        fields = '__all__'
        exclude = ['slug', 'status']
        widgets = {
            'investor_type': Select(attrs={'class': 'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'surname': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'linkedin_address': TextInput(attrs={'class': 'form-control', 'placeholder': 'https://linkedin/in/..'}),
            'country': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'employment_status': TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g Self employed'}),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g CEO'}),
            'bio': Textarea(attrs={'cols': 10, 'rows': 3, 'class': 'form-control', 'placeholder': 'Describe yourself in 300 words'}),
            'experience': Textarea(attrs={'cols': 10, 'rows': 3, 'class': 'form-control', 'placeholder': 'Descrie your experience in 300 words'}),
            'reason': Textarea(attrs={'cols': 10, 'rows': 3, 'class': 'form-control'}),
        }


class InvestorEditForm(ModelForm):
    class Meta:
        model = Investor
        fields = '__all__'
        exclude = ['slug']
        widgets = {
            'investor_type': Select(attrs={'class': 'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'surname': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'linkedin_address': TextInput(attrs={'class': 'form-control'}),
            'country': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'employment_status': TextInput(attrs={'class': 'form-control'}),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g CEO'}),
            'bio': Textarea(attrs={'cols': 10, 'rows': 3, 'class': 'form-control'}),
            'experience': Textarea(attrs={'cols': 10, 'rows': 3, 'class': 'form-control'}),
            'reason': Textarea(attrs={'cols': 10, 'rows': 3, 'class': 'form-control'}),
            'status': Select(attrs={'class': 'form-control'})
        }


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ['slug', 'read']
        widgets = {
            'user': Select(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'example@mail.com'}),
            'subject': TextInput(attrs={'class': 'form-control'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell us about your payment sales'}),
        }
