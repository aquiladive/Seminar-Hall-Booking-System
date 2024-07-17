from datetime import datetime, timedelta
from calendar import HTMLCalendar
from sbhs_app.models import event

global diff
diff = 0
global cont
cont = False
global longEvent

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None, location=None):
		self.year = year
		self.month = month
		self.location = location
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(startdate__day=day, hall=self.location, approval="True")
		d = ''

		global cont
		global diff
		global longEvent
		if cont and diff >= 0:
			d += f'<li><a data-bs-toggle="modal" data-bs-target="#desc{longEvent.id}-modal">{longEvent.dept}: {longEvent.name} ({longEvent.time})</a></li>'			
			diff -= 1
			if diff == 0:
				cont = False
				# diff = (event.enddate - event.startdate).days
				# i = 0
				# while i < diff:
				# 	d += f'<li><a data-bs-toggle="modal" data-bs-target="#desc{event.id}-modal">{event.dept}: {event.name} ({event.time})</a></li>'
				# 	i += 1

		for event in events_per_day:
			d += f'<li><a data-bs-toggle="modal" data-bs-target="#desc{event.id}-modal">{event.dept}: {event.name} ({event.time})</a></li>'
			d += f'<div class="modal" id="desc{event.id}-modal" aria-hidden="true"><div class="modal-dialog"><div class="modal-content"><div class="modal-header"><h5 class="modal-title">Event Description</h5><button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button></div><div class="modal-body">{event.description}</div></div></div></div>'
			if event.enddate > event.startdate:
				cont = True
				diff = (event.enddate - event.startdate).days
				longEvent = event 


		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td style="background-color:grey;"></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = event.objects.filter(startdate__year=self.year, startdate__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal
	
	

def eventVerify(newEvent):
	today = datetime.date(datetime.today())
	eventStartDate = newEvent.startdate
	eventEndDate = newEvent.enddate

	#if event is being booked for a past date
	if today > eventStartDate or today > eventEndDate:
		return 1
	
	#if event is being booked when other events have already been booked
	eventList = event.objects.filter(startdate=eventStartDate)
	for e in eventList:
		if e.time == newEvent.time:
			return 2
	
	eventList = event.objects.filter(enddate=eventStartDate)
	for e in eventList:
		if e.time == newEvent.time:
			return 2

	eventList = event.objects.filter(enddate=eventEndDate)
	for e in eventList:
		if e.time == newEvent.time or e.time == "9AM-5PM":
			return 2

	eventList = event.objects.filter(enddate=eventStartDate)
	for e in eventList:
		if e.time == newEvent.time or e.time == "9AM-5PM":
			return 2
		
	#if event is being booked on Sunday
	#if eventDate.strftime("%A")=='Sunday':
	#	return 3

	return 0