import datetime
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def car(request):
    return render(request,'car.html')

def bike(request):
    return render(request,'bike.html')


def hello(request):
   today = datetime.datetime.now().date()
   return render(request, "hello.html", {"todaydate" : today})

def hello1(request):
   today = datetime.datetime.now().date()
   return render(request, "hello1.html", {"todaydate" : today})


def hello2(request):
   today = datetime.datetime.now().date()
   
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "hello2.html", {"today" : today, "days_of_week" : daysOfWeek})



def evenodd(request):
   
   a = 25
   b = 25
   
   return render(request, "even.html" , {'c':a,'d':b})
