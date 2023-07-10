from django.shortcuts import render
from calendar import monthcalendar

def calendar_view(request, year, month):
    
    year, month = int(year), int(month)
    calendar_month = monthcalendar(int(year), int(month))
    calendar_data = {'calendar_month' : calendar_month, 'year' : year, 'month' : month}

    return render(request, './calendar.html', calendar_data)

def index(request):
    return render(request, './index.html')