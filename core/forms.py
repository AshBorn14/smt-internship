from django import forms
from .models import Application

INPUT_CLASSES = 'form-control border border-dark-subtle mt-1 mb-0'

class AddApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        exclude = ("created_at","isAccepted","infoVerified", "isRejected")

        widgets = {
            'startup_name':forms.TextInput(attrs={'class':INPUT_CLASSES}),
            'founder_name': forms.TextInput(attrs={'class':f'{INPUT_CLASSES}'}),
            'gender':forms.Select(attrs={'class':'form-select border border-dark-subtle mt-1 mb-2'}),
            'qualifications':forms.TextInput(attrs={'class':INPUT_CLASSES,'placeholder':'Please Enter Your Highest Qualification'}),
            'contact_number':forms.NumberInput(attrs={'class':INPUT_CLASSES}),
            'email_id': forms.EmailInput(attrs={'class':INPUT_CLASSES}),
            'institution_attended':forms.TextInput(attrs={'class':INPUT_CLASSES}),
            'founders_experience':forms.TextInput(attrs={'class':INPUT_CLASSES}),
            'product_name': forms.TextInput(attrs={'class':INPUT_CLASSES}),
            'brief_description': forms.Textarea(attrs={'class':INPUT_CLASSES, 'rows':3}),
            'incorporation_date':forms.DateInput(attrs={'class':INPUT_CLASSES}),
            'incorporation_certificate':forms.FileInput(attrs={'class':INPUT_CLASSES}),
            'website':forms.URLInput(attrs={'class':INPUT_CLASSES}),
            'address_of_company':forms.Textarea(attrs={'class':INPUT_CLASSES, 'rows':3}),
            'company_sector':forms.TextInput(attrs={'class':INPUT_CLASSES}),
            'technology_area':forms.TextInput(attrs={'class':INPUT_CLASSES}),
            'company_stage':forms.Select(attrs={'class':'form-select border border-dark-subtle mt-1 mb-2'}),
            'target_market':forms.Textarea(attrs={'class':INPUT_CLASSES, 'rows':3}),
            'usp':forms.Textarea(attrs={'class':INPUT_CLASSES, 'rows':3}),
            'revenue_streams':forms.Textarea(attrs={'class':INPUT_CLASSES, 'rows':3}),
            'pitchdeck':forms.FileInput(attrs={'class':INPUT_CLASSES,},),
            # 'infoVerified':forms.CheckboxInput(attrs={'class':'form-check form-input '})
        }
        labels = {
            'startup_name':'Startup Name / Name of Company',
            'founder_name':'Founder Name',
            'qualifications':'Qualifications of Founder (Pursuing or Completed)',
            'contact_number':'Contact Number',
            'email_id': 'Email',
            'institution_attended':'Institution Enrolled Presently or Last Attended',
            'founders_experience':'Total Industry/Research Experience of Founder with details',
            'product_name': 'Name of the product or service (if any)',
            'usp':'USP (Unique Value Proposition)',
        }
        
       

