import datetime 

def CurrentNorwegianMonths():
	nor_months = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]
	month = datetime.datetime.now().strftime("%m")

	return nor_months[int(month)-1]

