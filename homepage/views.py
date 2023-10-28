from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from homepage.form import filterForm
from homepage.models import Filter
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Filter
# Create your views here.



def homePageView(request):
    data = {
        'title' : 'WELCOME',
        'Begin' : 'Start'
    }
    return render(request, "index.html", data)


# using django form 
def add_filter(request):
    submitted = False
    if request.method == 'POST':
        form = filterForm(request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_filter?submitted=True')
    else:
        form = filterForm
        if 'submitted' in request.GET:
            submitted = True
        
    return render(request, 'filters/inputs.html', {'form': form, 'submitted' : submitted})

# #link to the add_filter to the nav bar
# <li class = 'nav-item'>
#     <a class = 'nav-link' href = "{% url 'filters/add_filter' %}"> add_filter</a>
# </li>


def resultPageView(request):
    results_list = Filter.objects.all()
    return render(request, 'filters/filter_results.html', {'result_list': results_list} )


