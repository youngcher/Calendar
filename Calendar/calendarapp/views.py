from django.shortcuts import render
from calendar import monthcalendar, month_name, Calendar

def calendar_view(request, year, month):
    
    year, month = int(year), int(month)

    custom_calendar = Calendar(firstweekday=6) # 일요일부터 시작하는 달력을 생성
    calendar_month = list(custom_calendar.monthdatescalendar(year, month)) # 달력에서 월의 날짜를 가져옵니다.

    calendar_data = {'calendar_month' : calendar_month, 'year' : year, 'month' : month}

    return render(request, './calendar.html', calendar_data)


def index(request):
    return render(request, './index.html')

