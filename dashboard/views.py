from tkinter import Y
from django.shortcuts import render, HttpResponse, redirect
from .forms import DataForm
from .models import Data
from .utils import get_plot
import numpy as np

# Create your views here.
def index(request):
    return render(request, 'index.html', )
    #return HttpResponse("this is home")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about")

def predictmodel(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-prediction')
    else:
        form = DataForm()
    context = {
        'form':form,
    }
    return render(request, 'predictmodel.html', context)

def prediction(request):
    predicted_consumption = Data.objects.all()
    context = {
        'predicted_consumption' : predicted_consumption
    }
    return render(request, 'prediction.html', context)
    #return HttpResponse("this is contact", context)

def consumption(request):
    qs = Data.objects.all()
    x = [x.year for x in qs]
    y = [y.consumption for y in qs]
    chart = get_plot(x, y)
    return render(request, 'consumption.html', {'chart':chart})

def cintactus(request):
    return render(request, 'cintactus.html')