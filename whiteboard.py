from gpio import *

def pressureSensor():
	top , bottom, seat =2,3,4
	topPressure = analogRead(top)
	bottomPressure = analogRead(bottom)
	seatPressure = analogRead(seat)
	
	return (topPressure, bottomPressure, seatPressure)



