from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from core.forms import Work_Details, ContactForm2


class ContactWizard(SessionWizardView):
    form_list = [Work_Details, ContactForm2]
    template_name = 'wizard_form.html'

    def done(self, form_list, **kwargs):
        do_something_with_the_form_data(form_list)
        return HttpResponseRedirect('/page-to-redirect-to-when-done/')
