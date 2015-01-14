# gpio.py
# by David Simon (dasimon@andrew.cmu.edu), January 2015

# This module sets up Python functions to utilize GPIO on the pcDuino

# It handles:
# Pin setup (pinMode)
# Digital input (digitalRead)
# Digital output (digitalWrite)
# Analog input (analogRead)

# It is based on the Arduino language as well as the following pcDuino tutorial
# https://learn.sparkfun.com/tutorials/programming-the-pcduino#accessing-gpio-pins

####################################################################
# SETUP - called automatically when the module is imported
####################################################################

import os

# store the paths of the pin mode and pin out mode
# gpio
GPIO_MODE_PATH = os.path.normpath('/sys/devices/virtual/misc/gpio/mode/')
GPIO_PIN_PATH = os.path.normpath('/sys/devices/virtual/misc/gpio/pin/')
GPIO_FILENAME = 'gpio'
# analog in (adc = analog -> digital conversion)
ADC_PATH = os.path.normpath('/proc/')
ADC_FILENAME = 'adc'

# create arrays to point to the files
pinModeFiles = []
pinDataFiles = []
adcFiles = []

# create variables to translate pin instructions to file I/O
HIGH = 1
LOW = 0
INPUT = 0
OUTPUT = 1
INPUT_PU = 8 # input with pull-up resistor

# store the maximum value for each channel of PWM
pwmMaxVal = []

# populate the arrays with file paths
for pinNumber in xrange(18):
    filename = GPIO_FILENAME + str(pinNumber)
    pinModeFiles.append(os.path.join(GPIO_MODE_PATH, filename))
    pinDataFiles.append(os.path.join(GPIO_PIN_PATH, filename))
for analogPinNumber in xrange(6):
    adcPinFile = ADC_FILENAME + str(analogPinNumber)
    adcFiles.append(os.path.join(ADC_PATH, adcPinFile))

####################################################################
# Function Definitions
####################################################################

def pinMode(pinNumber, mode):
    """
    Set the specified pin to the specified mode.
    Requires pin number in the range 0-17, inclusive, keyword for mode
    """
    filename = pinModeFiles[pinNumber]
    with open(filename, 'wt') as f:
        f.write(str(mode))

def digitalWrite(pinNumber, value):
    """
    Write the specified value to the specified pin
    Requires int pin number in the range 0-17, inclusive, keyword for value
    """
    filename = pinDataFiles[pinNumber]
    with open(filename, 'wt') as f:
        f.write(str(value))

def digitalRead(pinNumber):
    """
    Read the logic value from the specified pin
    Requires int pin number in the range 0-17, inclusive
    Returns integer 0 or 1 corresponding to logic value of pin
    """
    filename = pinDataFiles[pinNumber]
    with open(filename, 'rt') as f:
        value = f.read(1)
    return int(value)

def analogRead(pinNumber):
    """
    Return integer value read at adc pin.
    Requires int pin number in the range 0-5, inclusive
    for channels 0 and 1, returns
    """
    filename = adcFiles[pinNumber]
    with open(filename, 'rt') as f:
        value = f.read(1)
    return int(value)
