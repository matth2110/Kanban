"""
Customizations for the Django administration interface.
"""

from django.contrib import admin
from KanbanApp.models import Ticket

admin.site.register(Ticket)

