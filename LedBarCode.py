#!/usr/bin/python

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

leds = [3,5,7,10,11,13,15,16,18]

for led in leds:
    GPIO.setup(led, GPIO.OUT, initial=0)

time.sleep(1)

while True:

    for led in leds:
       GPIO.output(led, 1) # ON
       time.sleep(0.1)
       GPIO.output(led, 0) # OFF
