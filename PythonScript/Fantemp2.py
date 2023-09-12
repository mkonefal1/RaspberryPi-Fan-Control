import RPi.GPIO as GPIO
from vcgencmd import Vcgencmd
import getopt
import sys

pin = 14
temp_limit = 50.0

vcgm = Vcgencmd()
cputemp = vcgm.measure_temp()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pin, GPIO.OUT)

# I've changed the code to allow the fan to work on a determine temperature range.
# This is to avoid continuous turning the fan on and off when it is around the original desired temperature. I set the temp_limit to 50.
if cputemp < temp_limit:
    GPIO.output(pin, GPIO.LOW)

else:
    if cputemp > temp_limit:
        GPIO.output(pin, GPIO.HIGH)
