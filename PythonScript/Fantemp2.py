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

if cputemp < temp_limit:
    GPIO.output(pin, GPIO.LOW)

else:
    if cputemp > temp_limit:
        GPIO.output(pin, GPIO.HIGH)
