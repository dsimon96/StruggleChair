# STRUGGLE CHAIR -- BUILD18 JAN 2015
# Built and coded by rmehndir, vrramesh, dasimon, and sgakhar
# CMU ECE c/ 2018

class StruggleChair(object):

	def __init__(self, topPin, bottomPin, lbServo,
				 rbServo, ltServo, rtServo):
		self.topPin, self.bottomPin = topPin, bottomPin
		 # pins for pressure clusters
		self.servoPins = [lbServo, rbServo, ltServo, rtServo]
		# left bottom, right bottom, left top, right top

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