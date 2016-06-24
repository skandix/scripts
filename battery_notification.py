import easygui as g

def get_latest_N(n):
		for i in open('/sys/class/power_supply/BAT1/'+n+'', 'r'):
			return i.replace("\n", "")
			
def main():
	while True:
		try:
			if get_latest_N("capacity") == "15" and get_latest_N("status") == "Discharging":
				g.msgbox("You're getting low on Juice, please insert the charger", 'Battery')

			else:
				return "nothing"
		except:
			pass
while  True:
	main()
