from datetime import datetime
from datetime import date
def calculate_age(dob):
	print int((datetime.now() - datetime.strptime(dob,"%d/%m/%Y")).days/365), "Years"


def days_left_for_birth_day(born):
	day, month, year =[int(x) for x in born.split("/")]
	born = date(year, month, day)
	today = date.today()
	born_New=date(today.year,month,day)
	diff = abs((born_New-today).days)
	return diff

	
