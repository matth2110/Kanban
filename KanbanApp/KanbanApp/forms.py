"""
Definition of forms.
"""

from django import forms
from KanbanApp.models import Ticket
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
           'ticket_number',
           'ticket_description',
           'open_date',
           'hours_to_complete',
           'status',
           ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ticket_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['hours_to_complete'].widget.attrs.update({'class': 'form-control'})
        self.fields['open_date'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'YYYY-MM-DD'})
        self.fields['ticket_description'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})

    
        
        #fields['open_date'].widget.attrs.update({'placeholder': 'date'})
        
        #fields['ticket_description']=forms.CharField(label=_("Description"),
         #                                            widget=forms.TextInput({
          #                                               'class' : 'form-control'}))
        
        
