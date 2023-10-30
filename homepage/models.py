from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from datetime import datetime
import django.core.exceptions as Exceptions
import django.db.utils as dbExceptions

class Filter(models.Model):
    try:
        DepartureDate  = models.DateField( "DepartureDate",  null = False, blank = False)
        ReturnDate = models.DateField( "ReturnDate", null = False, blank = False)
        #Destination = destinationField()
        City = models.CharField('City', max_length= 30, null = False, blank = False)
        State = models.CharField('State',max_length= 30, null = False, blank = False)
        Country = models.CharField('Country', max_length= 30,null = False, blank = False)
        NumberOfTraveler = models.IntegerField('NumberOfTraveler',null = False, blank = False)
        BudgeMin = models.IntegerField('BudgeMin' )
        BudgetMax = models.IntegerField('BudgetMax',null = False, blank = False)

    except Exceptions.ValidationError:
        print("date format must be in YYYY-MM-DD format.'")
    
    except dbExceptions.IntegrityError:
        print("Must input all required values")


    def __str__(self):
        return self.DepartureDate.strftime("%m/%d/%Y") + "-" + self.ReturnDate.strftime("%m/%d/%Y") + ", " + self.City + " " + self.State
    




## error: self.widgets_names = ["_%s" % i for i in range(len(widgets))]
##        TypeError: object of type 'destinationWidget' has no len()
# class destinationWidget(forms.MultiWidget):
#     def __init__(self, *args, **kwargs):
#         widgets = [
#             forms.TextInput(),
#             forms.TextInput(),
#             forms.TextInput(),
#         ]
#         super().__init__(self,*args, **kwargs)

#     def decompress(self, value):
#         if value:
#             return value.split(' ')
#         return [None, None]

# class destination:
#     def __init__(self, City, state, country):
#         self.city = City
#         self.state = state
#         self.country = country

# class destinationField(forms.MultiValueField):
#     widgets = destinationWidget()
#     def __init__(self,widgets=widgets, *args , **kwargs):  
#         error_messages = {
#             "incomplete": "Enter a city name, state, and country.",
#         }
#         fields = (
#             models.CharField("city", max_length= 30),
#             models.CharField("state", max_length= 30),
#             models.CharField("country", max_length= 20) 
#         )
#         super().__init__(self, fields=fields,widgets=widgets, error_messages = error_messages, require_all_fields=False, **kwargs)
        
        

#     def compress(self, data_list):
#         City, state, country = data_list
#         return destination(City, state, country)
