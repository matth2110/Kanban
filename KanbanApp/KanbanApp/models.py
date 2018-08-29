"""
Definition of models.
"""

from django.db import models
from django.forms import ModelForm

# Create your models here.
class Ticket(models.Model):
    statuses = (('Research', 'Reasearch'),
                ('Coding', 'Coding'),
                ('QA', 'QA'),
                ('UAT', 'UAT'),
                ('Staging', 'Staging'),
                ('Completed', 'Completed')
                )
    ticket_number = models.IntegerField(primary_key= True, unique=True)
    open_date = models.DateField()
    ticket_description = models.TextField(max_length=300)
    hours_to_complete = models.IntegerField()
    status = models.CharField(max_length=10, choices=statuses, default='Research')

    def __str__(self):
        """Returns a string representation of a poll."""
        return self.ticket_description

