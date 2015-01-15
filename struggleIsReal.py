# STRUGGLE CHAIR -- BUILD18 JAN 2015

# Built and coded by rmehndir, vrramesh, dasimon, and sgakhar
# CMU ECE c/ 2018

from gpio import *
import requests
import time

class StruggleChair(object):

	def __init__(self):

		# SET UP ALARM (in seconds)
		self.alarmTime = 300 # 5 minutes for demo purposes
		self.alarm

		# SET UP SESSION END TIMER (in seconds)
		self.sessionWait = 30 # waits 1/2 minute before expiring session

		# SET UP PRESSURE SENSORS
		self.topPin = 2 # pin for top back FSR cluster
		self.bottomPin = 3 # pin for bottom back FSR cluster
		self.seatPin = 4 # pin for seat FSR cluster
		self.threshLow = 50 # threshold indicating insufficient pressure
		self.threshHigh = 750 # threshold indicating being pushed

		# SET UP SERVOS
		self.topServos = (1,2) # left/right in tuple
		self.bottomServos = (3,4)

		# SET UP THERMISTORS
		self.topTherm = 0
		self.bottomTherm = 1
		# low res analog pins for thermistor clusters

		# SET UP SOUND SENSOR
		# SET UP PIR MOTION SENSOR

		# SET UP VIBRATION MOTORS
		self.upperMotor = 5 # pin corresponding to upper motor
		self.lowerMotor = 6 # pin corresponding to lower motor

	def initSession(self):
		self.session = True
		time = time.time()
		self.alarm = time + self.alarmTime

	def endSession(self):
		self.session = False
		self.alarm = None