# STRUGGLE CHAIR -- BUILD18 JAN 2015

# Built and coded by rmehndir, vrramesh, dasimon, and sgakhar
# CMU ECE c/ 2018

from gpio import *
import requests

class StruggleChair(object):

	def __init__(self):

		# SET UP ALARM (in seconds)
		self.alarmTime = 300 # 5 minutes for demo purposes

		# SET UP SESSION END TIMER (in seconds)
		self.sessionWait = 30 # waits 1/2 minute before expiring session

		# SET UP PRESSURE SENSORS
		self.topPin = 0 # pin for top back FSR cluster
		self.bottomPin = 1 # pin for bottom back FSR cluster
		self.seatPin = 2 # pin for seat FSR cluster
		self.threshLow = 50 # threshold indicating insufficient pressure
		self.threshHigh = 750 # threshold indicating being pushed

		# SET UP SERVOS
		self.topServos = (1,2) # left/right in tuple
		self.bottomServos = (3,4)

		# SET UP THERMISTORS
		# SET UP SOUND SENSOR
		# SET UP PIR MOTION SENSOR

		# SET UP VIBRATION MOTORS
		self.upperMotor = 5 # pin corresponding to upper motor
		self.lowerMotor = 6 # pin corresponding to lower motor



	def initSession(self):
		self.session = True
		self.alarm = None

	def endSession(self):
		self.session = False

	def read(self):
		# calls all sensors and adjusts variables

	def pressure(self):
		# get pressure from top cluster
		# get pressure from bottom cluster
		# stores output in self.topPressure and self.bottomPressure

	def parse(self):
		# checks sensor variables
		# adjusts accordingly

	def moveTop(self):
		# uses servos to move chair's back (top)

	def moveBottom(self):
		# uses servos to move chair's back (bottom)