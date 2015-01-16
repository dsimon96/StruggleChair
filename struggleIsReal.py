# STRUGGLE CHAIR -- BUILD18 JAN 2015

# Built and coded by rmehndir, vrramesh, dasimon, and sgakhar
# CMU ECE c/o 2018

from gpio import *
import requests
import time

class StruggleChair(object):

	def __init__(self):

		# OVERALL SETUP
		self.session = False

		# SET UP ALARM (in seconds)
		self.alarmTime = 300 # 5 minutes for demo purposes
		self.alarm = None

		# SET UP SLEEP WAITING (in seconds)
		self.sleepy = False
		self.sleepWait = 120 # 2 minutes of sleepy time

		# SET UP SESSION END TIMER (in seconds)
		self.sessionWait = 30 # waits 1/2 minute before expiring session

		# SET UP PRESSURE SENSORS
		self.topPin = 2 # pin for top back FSR cluster
		self.topPressure = 0
		self.bottomPin = 3 # pin for bottom back FSR cluster
		self.bottomPressure = 0
		self.seatPin = 0 # pin for seat FSR cluster
		self.seatPressure = 0
		self.seatThreshold = 10 # threshold that someone is seated
		self.topRange = (250, 500) # range for good posture
		self.bottomRange = (100, 400)

		# SET UP THERMISTORS
		self.initTemp = None
		self.topTherm = 4
		self.topHeat = 0
		self.bottomTherm = 5
		self.bottomHeat = 0
		# high res analog pins for thermistor clusters

		# SET UP SOUND SENSOR
		self.soundPin = 1 # low res (6-bit integer)
		self.amplitude = 0

		# SET UP VIBRATION MOTORS (digital pins)
		self.upperMotor = 4 # pin corresponding to upper motor
		self.lowerMotor = 5 # pin corresponding to lower motor
		pinMode(self.upperMotor, OUTPUT)
		pinMode(self.lowerMotor, OUTPUT)

		# SET UP LED PINS
		self.forwardLED = 6 # indicates leaning too far forward
		self.greenLED = 7
		self.backLED = 8 # indicates leaning too far back
		pinMode(self.forwardLED, OUTPUT)
		pinMode(self.greenLED, OUTPUT)
		pinMode(self.backLED, OUTPUT)

	def getSound(self):
		self.amplitude = analogRead(self.soundPin)

	def getHeat(self):
		self.topHeat = analogRead(self.topTherm)
		self.bottomHeat = analogRead(self.bottomTherm)

	def startSession(self):
		self.session = True
		time = time.time()
		self.sessionStart = time
		self.alarm = time + self.alarmTime
		self.getHeat
		self.initTemp = (self.topHeat + self.bottomHeat)/2

	def endSession(self):
		self.session = False
		self.alarm = None
		time = time.time()
		self.sessionEnd = time

	def checkTop(self):
		self.topPressure = analogRead(self.topPin)

	def checkBottom(self):
		self.bottomPressure = analogRead(self.bottomPin)

	def checkSeat(self):
		self.seatPressure = analogRead(self.seatPin)

	def lightLED(self, pin):
		digitalWrite(self.forwardLED, LOW)
		digitalWrite(self.greenLED, LOW)
		digitalWrite(self.backLED, LOW)
		digitalWrite(pin, HIGH)

	def ring(self):
		# hardcoded right now- no option but to get off
		# for the sake of demo speed
		for x in xrange(10):
			digitalWrite(self.lowerMotor, HIGH)
			digitalWrite(self.upperMotor, HIGH)
			time.sleep(2)
			digitalWrite(self.lowerMotor, LOW)
			digitalWrite(self.upperMotor, LOW)
			time.sleep(.5)
		self.endSession()

	def checkSleepiness(self):
		self.getHeat()
		if (self.topHeat < (self.initTemp - 400) and
			self.bottomHeat < (self.initTemp - 400)):
			self.sleepy = True
		else:
			self.sleepy = False

	def wake(self):
		while self.sleepy()

	def run(self):
		while True:
			if self.session:
				time = time.time()
				if self.alarm and time > self.alarm:
					self.ring()
				if self.sleepAlarm and time > self.sleepAlarm:
					self.wake()
			else:
				while self.seatPressure < 10:
					self.checkSeat()
				self.startSession()
