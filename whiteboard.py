from gpio import *
import time

def pressureSensor():
	#top , bottom, seat =2,3,4
	top = 2	
	topPressure = analogRead(top)
	#bottomPressure = analogRead(bottom)
	#seatPressure = analogRead(seat)
	
	#return (topPressure, bottomPressure, seatPressure)
	return topPressure

while(True):
	print pressureSensor()
	time.sleep(1)
