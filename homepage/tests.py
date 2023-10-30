from django.test import TestCase, client 
import pytest
from .models import Filter
from .form import filterForm
import django.core.exceptions as Exceptions
import django.db.utils as dbExceptions
from http import HTTPStatus

print("Unit Testing")
class TestModel(TestCase):

#2023-10-11
    def test_model_self_1(self):
        print("test 1")
        try:
            test1 = Filter.objects.create(DepartureDate ="2023-10-11", ReturnDate = "10/22/2023", City = 'Brooklyn', State = 'NY', Country = 'USA', NumberOfTraveler = '2', BudgeMin = '2', BudgetMax = '3' )                
        except Exceptions.ValidationError:
            print("failed, date format must be in YYYY-MM-DD format.")
            return 
        #self.assertEqual(str(test1.City), "Brooklyn")
        assert (test1.City) == "NY"
    
       
#"2023-10-22"
    def test_model_self_2(self):
        print('\ntest2')
        test2 = Filter.objects.create(DepartureDate ="2023-10-11", ReturnDate = "2023-10-22", City = 'Brooklyn', State = 'NY', Country = 'USA', NumberOfTraveler = '2', BudgeMin = '2', BudgetMax = '3' )
        self.assertEqual(str(test2.ReturnDate), "2023-10-22")


            
##################
# before running test coverage report 
# Name                Stmts   Miss  Cover
# ---------------------------------------
# homepage\tests.py       5      2    60%
# ---------------------------------------
# TOTAL                   5      2    60%

# Name                Stmts   Miss  Cover
# ---------------------------------------
# homepage\tests.py      18     15    17%
# ---------------------------------------
# TOTAL                  18     15    17%


print("\nintegration test:\n")
## integration test:
# testing filterForm:

class TestFilterForm(TestCase):

    def test_form_valid(self):     
        print('\nTesting if form is valid: ', end = '')

        filter_data = {
            'DepartureDate' : '2023-10-30',
            'ReturnDate' : '2023-11-11',
            'City' : 'New York',
            'State' : 'NY',
            'Country' : 'US',
            'NumberOfTraveler' : '2',
            'BudgeMin' : '2',
            'BudgetMax' :  '100'
        }
        name_form = filterForm(data=filter_data)
        self.assertTrue(name_form.is_valid())
        print("passed form is valid test")

    def test_form_valid2(self):
        print('\nTesting if valid when required input section is missing: ', end = '')
        filter_data2 = {
            'DepartureDate' : '2023-10-30',
            'ReturnDate' : '2023-11-11',
            'City' : 'New York',
            'State' : 'NY',
            'Country' : 'US',
            'NumberOfTraveler' : '2',
            'BudgeMin' : '2',
            'BudgetMax' :  ''
        }
        
        name_form2 = filterForm(data=filter_data2)
        
        self.assertTrue(name_form2.is_valid())

    def test_form_html(self):
        print("\nTesting if html works, will redirect if works: ", end = '')
        filter_data3 = {
            'DepartureDate' : '2023-10-30',
            'ReturnDate' : '2023-11-11',
            'City' : 'New York',
            'State' : 'NY',
            'Country' : 'US',
            'NumberOfTraveler' : '2',
            'BudgeMin' : '2',
            'BudgetMax' :  '100'
        }
        response = self.client.post("/add_filter", data= filter_data3)

        self.assertEqual(response.status_code, 302)
        print("Yes, redicted")


    def test_form_html2(self):
        print("\nTesting if html works, required input is missing: ", end = '')
        filter_data4 = {
            'DepartureDate' : '2023-10-30',
            'ReturnDate' : '2023-11-11',
            'City' : '',
            'State' : 'NY',
            'Country' : 'US',
            'NumberOfTraveler' : '2',
            'BudgeMin' : '2',
            'BudgetMax' :  '100'
        }
        response = self.client.post("/add_filter", data= filter_data4)

        self.assertEqual(response.status_code, 302)
        print("Yes, redicted")



