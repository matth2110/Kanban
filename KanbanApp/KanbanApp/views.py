"""
Definition of views.
"""
from KanbanApp.models import Ticket
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, FormView
from KanbanApp.forms import CreateTicketForm

class TicketCreateView(FormView):
    form_class = CreateTicketForm
    template_name = "app/createTicket.html"
    success_url = "/tickets/"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create a ticket'
        return context
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def tickets(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tickets.html',
        {
            'title':'Open Tickets',
            'message':'All open tickets.',
            'year':datetime.now().year,
        }
    )

class TicketListView(ListView):
    template_name = 'app/tickets.html'
    # model = Ticket (accomplishes the same as below)
    queryset = Ticket.objects.all() #This can be filtered down, the html
                                    #just looks for object_list which is
                                    #produced by the ListView template
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Open Tickets'
        return context
    
