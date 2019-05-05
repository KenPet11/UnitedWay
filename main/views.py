from datetime import datetime, timedelta, date
from time import time
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from django.urls import reverse
import calendar
from .models import *
from .utils import Calendar
from .forms import EventForm
from .forms import SignupForm
# Create your views here.

curr_date = datetime.today()

def get_state_date(state):
    global curr_date
    d = curr_date
    if state == 'PREV':
        da = str(d).split()[0].split('-')
        da[1] = '0' + str(int(da[1])-1)
        da = "-".join(str(x) for x in da)
        d = datetime.strptime(da, '%Y-%m-%d')
        curr_date = d
        return curr_date
    elif state == 'NEXT':
        da = str(d).split()[0].split('-')
        da[1] = '0' + str(int(da[1])+1)
        da = "-".join(str(x) for x in da)
        d = datetime.strptime(da, '%Y-%m-%d')
        curr_date = d
        return curr_date
    else:
        return curr_date

def index(request):
    return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'main/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

class CalendarNextView(generic.ListView):
    model = Event
    template_name = 'main/calendar_next.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        #d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        d = get_state_date('NEXT')
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

class CalendarPrevView(generic.ListView):
    model = Event
    template_name = 'main/calendar_prev.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        #d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        d = get_state_date('PREV')
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('main:calendar'))
    return render(request, 'main/event.html', {'form': form})

def signup(request, event_id=None):
    instance = Signup()
    if event_id:
        event = get_object_or_404(Event, pk=event_id)
        instance = Signup(event_name=event.event_title,e_description = event.event_description, 
            e_start_time = event.event_start_time,
            e_end_time = event.event_end_time,
            e_location = event.event_location,
            e_coordinator = event.event_coordinator,
            e_organization = event.event_organization,
            e_contact_email = event.event_contact_email,
            e_contact_phone = event.event_contact_phone,
            e_link = event.event_link)
    else:
        instance = Signup()
        
    form = SignupForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('main:calendar'))
    return render(request, 'main/signup.html', {'form': form})