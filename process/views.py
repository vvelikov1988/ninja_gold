from django.shortcuts import render, HttpResponse, redirect
import random

def home(request):
    if 'your_gold' not in request.session:
        request.session['your_gold'] = 0
    return render(request, 'index.html')

def process(request):
    return HttpResponse("This is the process page")

def farm_action(request):
    n = random.randint(10,20)
    request.session['your_gold'] +=n
    request.session['activities'] = f"You gained {n} coins"
    return redirect('/')

def cave_action(request):
    n = random.randint(5,10)
    request.session['your_gold'] +=n
    request.session['activities'] = f"You gained {n} coins"
    return redirect('/')

def house_action(request):
    n = random.randint(2,5)
    request.session['your_gold'] +=n
    request.session['activities'] = f"You gained {n} coins"
    return redirect('/')

def casino_action(request):
    n = random.randint(-50,50)
    request.session['your_gold'] +=n
    if n >= 0:
        request.session['activities'] = f"You gained {n} coins"
    else:
         request.session['activities'] = f"You lost {n} coins"
    return redirect('/')




