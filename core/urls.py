from core.views import ContactWizard
from core.forms import Work_Details, ContactForm2
from django.urls import path

urlpatterns = [
    path('form', ContactWizard.as_view([Work_Details, ContactForm2])),
]
