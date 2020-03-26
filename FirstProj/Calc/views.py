from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'form.html')

def add(request):
    #fetching the values
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    val3 = val1 + val2
    return render(request, 'result.html', {'ans':val3})


