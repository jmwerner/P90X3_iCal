# Install all modules. I used pip. Example:
# pip install datetime

from icalendar import Calendar, Event
from datetime import datetime, timedelta
from numpy import reshape
import pytz
import tempfile
import os


######
######
# Start Date - year, month, day, hour, minute, second
# Coded right now to last one hour and be added to calendar
#  at the same time every day until finished
start_date = datetime(2015, 1, 11, 6, 0, 0)
# Output directory
directory = '/your/directory/here'
######
######


# Function to print a rough view of the calendar to check if it's correct
def printcal(names, ord):
	n_weeks = int(len(ord) / 7) + 1
	mat = [0 for x in range(n_weeks * 7)]
	for i in range(len(ord)):
		mat[i] = names[ord[i] - 1]
	print(reshape(mat, (n_weeks,7)))

# Hard coded order of workouts (not the most efficient way, but it works!)

# This is the order for the "classic calendar"  http://rippedclub.net/wp-content/uploads/2013/12/P90X3-Classic-Calendar.png
order = [1,2,3,4,15,9,7, 
1,2,3,4,15,9,7,
1,2,3,4,15,9,7,
8,7,16,5,15,3,7,
10,17,3,11,6,12,7,
10,17,3,11,6,12,7,
10,17,3,11,6,12,7,
8,7,16,5,15,3,7,
13,2,4,3,17,1,7,
13,12,10,17,5,11,7,
13,2,4,3,17,1,7,
13,12,10,17,5,11,7,
8,16,5,3,7,7]

# New schedule for Ab Ripper (corresponding to classical calendar)
ab_ripper = [0,0,0,1,0,0,1,
0,0,0,1,0,0,1,
0,0,0,1,0,0,1,
0,1,0,0,0,0,1,
0,0,1,0,0,0,1,
0,0,1,0,0,0,1,
0,0,1,0,0,0,1,
0,1,0,0,0,0,1,
0,0,1,0,0,0,1,
0,0,1,0,0,0,1,
0,0,1,0,0,0,1,
0,0,1,0,0,0,1,
0,0,0,0,1,0]

# This is the order for the "mass calendar"
# order = [1,2,3,4,5,6,7, 
# 1,2,3,4,5,6,7,
# 1,2,3,4,5,6,7,
# 8,7,9,5,2,3,7,
# 10,11,3,10,11,12,7,
# 10,11,3,10,11,12,7,
# 10,11,3,10,11,12,7,
# 8,7,9,5,13,3,7,
# 10,11,3,10,11,12,7,
# 14,2,3,4,5,6,7,
# 10,11,3,10,11,12,7,
# 14,2,3,4,5,6,7,
# 8,3,13,11,10,7]

# This is the order for the "lean calendar"
# order = [16,9,3,15,8,2,7, 
# 16,9,3,15,8,2,7,
# 16,9,3,15,8,2,7,
# 8,7,16,5,2,3,7,
# 17,9,3,12,6,15,7,
# 17,9,3,12,6,15,7,
# 17,9,3,12,6,15,7,
# 8,7,16,5,15,3,7,
# 13,12,11,3,17,10,7,
# 12,13,17,5,13,15,7,
# 13,12,11,3,17,10,7,
# 12,13,17,5,13,15,7,
# 8,16,5,3,7,7]

# No Ab Ripper
# ab_ripper = [0 for i in range(90)]


# Names of workouts
workouts = ["Total Synergistics", "Agility X", "X3 Yoga", 
	"The Challenge", "Pilates X", "Incinerator", "Dynamix", 
	"Isometrix", "The Warrior", "Eccentric Upper",
	"Eccentric Lower", "MMX", "Decelerator",
	"Total Synergistics", "CVX", "Accelerator", "Triometrics"]

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
	# ab_ripper[x] ... hehe
	if ab_ripper[x]:
		event = Event()
		event.add('summary', 'Ab Ripper X3')
		event.add('dtstart', newday)
		event.add('dtend', newday + timedelta(hours=1))
		cal.add_component(event)


# Open file stream and dump to .ics file 
f = open(os.path.join(directory, 'X3.ics'), 'wb')
f.write(cal.to_ical())
f.close()



