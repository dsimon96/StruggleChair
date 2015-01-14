from gpio import *
import time 

outPin = 6

pinMode(outPin, OUTPUT)

while True:
	digitalWrite(outPin, HIGH)
	
	time.sleep(2) 
	
	digitalWrite(outPin, LOW)

	time.sleep(2)