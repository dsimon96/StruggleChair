# This file sets up functions to utilize the GPIO capabilities of the pcDuino
# It is based on the Arduino language as well as the following pcDuino tutorial
# https://learn.sparkfun.com/tutorials/programming-the-pcduino#accessing-gpio-pins

# store the paths of the pin mode and pin out mode
GPIO_MODE_PATH = os.path.normpath('/sys/devices/virtual/misc/gpio/mode/')
GPIO_PIN_PATH = os.path.normpath('/sys/devices/virtual/misc/gpio/pin/')
GPIO_FILENAME = 'gpio'

# create arrays to point to the files
pinMode = []
pinData = []

# create variables to translate pin instructions to file I/O
HIGH = '1'
LOW = '0'
INPUT = '0'
OUTPUT = '1'
INPUT_PU = '8' # input with pull-up resistor

# populate the arrays with file paths
for pinNumber in xrange(18):
    filename = GPIO_FILENAME + str(pinNumber)
    pinMode.append(os.path.join(GPIO_MODE_PATH, filename))
    pinData.append(os.path.join(GPIO_PIN_PATH, filename))

def pinMode(pinNumber, mode):
    """Set the specified pin to the specified mode"""
    filename = pinMode[pinNumber]
    with open(filename, 'wt') as file:
        file.write(mode)

def digitalWrite(pinNumber, value):
    """Write the specified value to the specified pin"""
    filename = pinData[pinNumber]
    with open(filename, 'wt') as file:
        file.write(value)

def digitalRead(pinNumber):
    """Read the logic value from the specified pin"""
    filename = pinData[pinNumber]
    with open(filename, 'rt') as file:
        value = file.read()
    return int(value)
    




