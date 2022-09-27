from ast import If
from calendar import month
from imghdr import tests

from django import http
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
# Create your views here.
from datetime import datetime
from datetime import date
from django.conf import settings
from django.shortcuts import redirect


def error_404_view(request, exception):

	# we add the path to the the 404.html file
	# here. The name of our HTML file is 404.html
	return render(request, '404.html')

def home(request):
    return render(request, 'home.html')


def year(request):

    current_year = datetime.now().year
    current_month =  datetime.now().month
    current_date = datetime.now().day
    current_hour = datetime.now().hour
    current_minutes = datetime.now().minute
    current_sec = datetime.now().second
    val1=  int(request.GET['year'])
    val2=  int(request.GET['month'])
    val3=int (request.GET['date'])
    d0 = date(val1, val2, val3)
    testt = int(current_date)
    d1 = date( current_year ,current_month,testt)
    delta = d1 - d0
    test1 = delta.max
    test2 = 12 - val2
    test3 = 24 - current_hour

    year = round((current_year - 1)- val1 )
    month = round(((year * 12) + current_month + test2))
    days = delta.days
    weeks = round(days / 7)
    hours = round( (days * 24) - test3 )   
    minutes = round ( ((hours - current_hour) * 60 )+ current_minutes)
    seconds = round ((( minutes - 1) * 60 ) + current_sec)
    error = 'please enter again'
    if current_month >= val2:
            years = year + 1
    
    if current_date <= val3 :
       years -= 1
   
    if val1 == 0  :
     return render(request ,'home.html' ,{'error' : error})
    return render(request, 'results.html',{'results' :years ,'Month': month , 'weeks' : weeks , 'date' : days, 'hours': hours 
    , 'minutes' :minutes , 'second' : seconds}) 
