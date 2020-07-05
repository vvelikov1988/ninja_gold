from django.shortcuts import render, HttpResponse, redirect
import random

def home(request):
    if 'your_gold' not in request.session:
        request.session['your_gold'] = 0
    return render(request, 'index.html')

def process(request):
    return HttpResponse("This is the process page")

def gold_count(request):
    if 'your_gold' not in request.session:
        request.session['your_gold'] = 10
    request.session['your_gold'] = random.randint(10,20)
    return render(request, 'index.html', 'gold_count')
    

def farm_action(request):
    n = random.randint(10,20)
    request.session['your_gold'] +=n
    return render(request, 'index.html')

def cave_action(request):
    n = random.randint(5,10)
    request.session['your_gold'] +=n
    return render(request, 'index.html')

def house_action(request):
    n = random.randint(2,5)
    request.session['your_gold'] +=n
    return render(request, 'index.html')

def casino_action(request):
    n = random.randint(-50,50)
    request.session['your_gold'] +=n
    if n >= 0:
        request.session['activites'] = "You gained f{n} coins"
    else:
         request.session['activites'] = "You lost f{n} coins"
    return render(request, 'index.html')




