from gpio import *
import time

def pressureSensor():
	top , bottom, seat =2,3,0
	topPressure = analogRead(top)
	bottomPressure = analogRead(bottom)
	seatPressure = analogRead(seat)
	
	return (topPressure, bottomPressure, seatPressure)

def blinkLed():
	topPressure, bottomPressure, seatPressure = pressureSensor()
	# top = 200 to 500 
	# bottom = 100 to 400
	# seat = 10 to 40
	ledGreen = 1
	if (topPressure >= 250 and topPressure <= 500) and (bottomPressure >= 100 and bottomPressure <= 400) and (seatPressure >10):
		pinMode(1,OUTPUT)	
		digitalWrite(ledGreen, HIGH)

def vibrationSensor():
	vibrationPin = 4
	pinMode(4, OUTPUT)
	digitalWrite(vibrationPin, HIGH)
 	
def soundSensor():
	soundPin = 5
	soundValue = analogRead(soundPin)
	return soundValue

def thermistorSensor():
	thermPin = 4
	thermVal = analogRead(thermPin)
	return thermVal

while(True):
	#blinkLed()
	#print pressureSensor()
	vibrationSensor()
	#print soundSensor()
	#print thermistorSensor()
	time.sleep(1)
	
 