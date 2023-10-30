from django.forms import ModelForm
from django import forms
from .models import Filter
from datetime import datetime

class filterForm(ModelForm):
   
    class Meta:
        model = Filter
        fields = ('DepartureDate', 'ReturnDate', 'City',"State", 'Country', 'NumberOfTraveler' ,'BudgeMin', 'BudgetMax' )
        labels = {
            'DepartureDate' : 'Departure Date',
            'ReturnDate' : 'Return Date',
            #Destination = destinationField()
            'City' : '',
            'State' : '',
            'Country' : '',
            'NumberOfTraveler' :'',
            'BudgeMin' : '',
            'BudgetMax' :  ''
        }
        now = datetime.now().date()
        current_date = now.strftime("%mm/%dd/%yyyy")
                                                                                                                                                               
        widgets = {
            'DepartureDate' : forms.DateInput(attrs={'type' : 'date', 'class': "form-controlr", 'data-date-format' :"mm/dd/yyyy", 'placeholder' :"Depature Date", 'required' : 'True', 'min':"<?php echo date('m/d/Y'); ?>"}),
            'ReturnDate' : forms.DateInput(attrs={'type' : 'date','class': 'form-contrl', 'data-date-format' :"mm/dd/yyyy", 'placeholder' :"Return Date", 'required' : 'True'}),
            #Destination = destinationField()
            'City' : forms.TextInput(attrs={'class': 'form-contrl', 'placeholder' :"City", 'required' : 'True'}),  
            'State' : forms.TextInput(attrs={'class': 'form-contrl', 'placeholder' :"State", 'required' : 'True'}),
            'Country' : forms.TextInput(attrs={'class': 'form-contrl', 'placeholder' :"Country", 'required' : 'True'}),
            'NumberOfTraveler' : forms.NumberInput(attrs={'class': 'form-contrl', 'placeholder' :"# Of Travelers", 'required' : 'True', 'min': 1}),
            'BudgeMin' : forms.NumberInput(attrs={'class': 'form-contrl', 'placeholder' :"Minimum amount", 'min' : '0'}),
            'BudgetMax' : forms.NumberInput(attrs={'class': 'form-contrl', 'placeholder' :"Maximum amount", 'required' : 'True'}),
        }



class Filter_results:
    resultList = Filter.objects.all()


    def __str__(self):
            return        