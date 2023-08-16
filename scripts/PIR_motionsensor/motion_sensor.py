import RPi.GPIO as GPIO
import time
import datetime

# GPIO pin
pir_sensor = 17
# Initialze GPIO 
GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_sensor, GPIO.IN)
# Set state of motion sensor in 0
current_state = 0
try:
    while True:
        time.sleep(0.1)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            print("Motion detected, PIN %s State %s at " % (pir_sensor, current_state) + str(datetime.datetime.now()))
        else:
            print("Wait motion, PIN %s State %s " % (pir_sensor, current_state)) 
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
