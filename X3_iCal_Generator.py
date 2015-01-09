# Install all modules. I used pip. Example:
# pip install datetime

from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz, tempfile, os

######
######
# Start Date - year, month, day, hour, minute, second
# Coded right now to last one hour and be added to calendar
#  at the same time every day until finished
start_date = datetime(2015, 1, 1, 6, 0, 0)
# Output directory
directory = '/my/directory/here'
######
######

# Hard coded order of workouts (not the most efficient way, but it works!)
order = [1,2,3,4,5,6,7, 
1,2,3,4,5,6,7,
1,2,3,4,5,6,7,
8,7,9,5,2,3,7,
10,11,3,10,11,12,7,
10,11,3,10,11,12,7,
10,11,3,10,11,12,7,
8,7,9,5,13,3,7,
10,11,3,10,11,12,7,
14,2,3,4,5,6,7,
10,11,3,10,11,12,7,
14,2,3,4,5,6,7,
8,3,13,11,10,7]

# Names of workouts
workouts = ["Total Synergistics", "Agility X", "X3 Yoga", 
	"The Challenge", "Pilates X", "Incinerator", "Dynamix", 
	"Isometrix", "The Warrior", "Eccentric Upper",
	"Eccentric Lower", "MMX", "Decelerator",
	"Total Synergistics"]

cal = Calendar()
cal.add('prodid', '-//My calendar product//mxm.dk//')
cal.add('version', '2.0')

for x in range(0,len(order)-1,1):
	event = Event()
	newday = start_date + timedelta(days=x)
	event.add('summary', workouts[order[x]-1])
	event.add('dtstart', newday)
	event.add('dtend', newday + timedelta(hours=1))
	cal.add_component(event)

# Open file stream and dump to .ics file 
f = open(os.path.join(directory, 'X3.ics'), 'wb')
f.write(cal.to_ical())
f.close()
