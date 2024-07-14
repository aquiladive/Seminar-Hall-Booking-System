from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from sbhs_app.models import user, adminUser, event
from sbhs.forms import userForm, eventForm
from sbhs.utils import Calendar, eventVerify


global deptuser
deptuser = ""

global adminuser
adminuser = ""

def home(request):
    return render(request, 'home.html')

def hall(request):
    return render(request, 'hall.html')

def about(request):
    return render(request, 'about.html')

def eventCal(request):
    return render(request, 'cal.html')

#login for dept page
def deptlogin(request):
    error = False
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            login_user = user.objects.filter(email=email, password=pwd)
            if(login_user):
                global deptuser
                deptuser = login_user.values_list("username", flat=True)[0]
                return render(request, 'dept.html', {"user":deptuser})
            else:
                error = True

            return render(request, 'deptlogin.html', {'form': form, 'error':error})
    else:
        form = userForm()

    return render(request, 'deptlogin.html', {'form': form, 'error':error})

def dept(request):
    global deptuser
    if deptuser!="":
        return render(request, 'dept.html', {"user":deptuser})
    else:
        return HttpResponse("<h3>Page cannot be accessed.</h3>")



#login for admin page
def adminlogin(request):
    error = False
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            login_user = adminUser.objects.filter(email=email, password=pwd)
            if(login_user):
                global adminuser
                adminuser = login_user.values_list("username", flat=True)[0]
                return render(request, 'admin.html', {"user":adminuser})
            else:
                error = True

            return render(request, 'adminlogin.html', {'form': form, 'error':error})
    else:
        form = userForm()

    return render(request, 'adminlogin.html', {'form': form, 'error':error})

def admin(request):
    global adminuser
    if adminuser!="":
        return render(request, 'admin.html', {"user":adminuser})
    else:
        return HttpResponse("<h3>Page cannot be accessed.</h3>")

def adminApprove(request):
    eventlist = event.objects.filter(approval="False")
    return render(request, 'adminapprove.html', {'event':eventlist})


def bookEvent(request):
    global deptuser
    errorList = [False, "Event date must be set in the future.", "The day's slots have already been booked, please choose another date.", "No events can be booked on a Sunday."]
    errorMsg = ""
    if deptuser!="":
        error = errorList[0]
        if request.method == 'POST':
            form = eventForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['event_name']
                date = form.cleaned_data['event_date']
                time = form.cleaned_data['timeSlot']
                desc = form.cleaned_data['event_description']
                hall = form.cleaned_data['event_hall']
                newEvent = event(name=name, date=date, time=time, description=desc, hall=hall, dept=deptuser, approval="False")
                verify = eventVerify(newEvent)
                if verify==0:
                    newEvent.save()
                    return render(request, 'book_success.html')
                else:
                    error = True
                    errorMsg = errorList[verify]
            else:
                error = True
                errorMsg = "There is an error in your form. Please retry."
        else:
            form = eventForm()
        return render(request, 'book_event.html', {'form': form, 'error':error, 'errorMsg':errorMsg, 'dept':deptuser})
    else:
        return HttpResponse("<h3>Page cannot be accessed.</h3>")

def bookSuccess(request):
    return render(request, 'book_success.html')


#calendar display for cal.html
class CalendarViewR(generic.ListView):
    model = event
    template_name = 'calfull_r.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('day', None))
        cal_ramegowda = Calendar(d.year, d.month, "Ramegowda")
        html_calr = cal_ramegowda.formatmonth(withyear=True)
        return {'calendar_r':mark_safe(html_calr)}

class CalendarViewT(generic.ListView):
    model = event
    template_name = 'calfull_t.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('day', None))
        cal_training = Calendar(d.year, d.month, "Training")
        html_calt = cal_training.formatmonth(withyear=True)
        return {'calendar_t':mark_safe(html_calt)}

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.today()