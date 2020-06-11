from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.core.exceptions import ValidationError
from core.models import Work_Details


class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()


class ContactForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea)


class Work_Details(forms.Form):
    def __init__(self, *args, **kwargs):
        super(Work_Details, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_show_errors = True

    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'enter job title '}))
    company = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'enter company name  '}))
    description = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'enter job description '}))
    location = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'enter location '}))
    start_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'],
                                     widget=forms.DateTimeInput(attrs={
                                         'class': 'form-control datetimepicker-input',
                                         'data-target': '#datetimepicker1'
                                     })
                                     )
    end_date = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'enter ending  date '}))
    current = forms.CharField(required=True)

    class Meta:

        model = Work_Details
        fields = '__all__'
