import psutil
import time
import subprocess as sc

while True:
	batt = psutil.sensors_battery()

	if batt.percent <= 40:
		sc.call(['notify-send', 'Battery Low', 'Please plug-in a charger Sir'])
	elif batt.percent >=80 and batt.power_plugged is True	:
		sc.call(['notify-send', 'Battery charged', 'Please remove the charger Sir'])
	
	for i in range(600):
		time.sleep(1)