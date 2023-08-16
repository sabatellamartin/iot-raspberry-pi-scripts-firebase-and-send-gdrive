import RPi.GPIO as GPIO
import datetime

GPIO_PIN = 25

class Movimiento():

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_PIN, GPIO.IN)

    def sensarMovimiento(self):
        current_state = GPIO.input(GPIO_PIN)
        if current_state == 1:
            #print("Movimiento detectado, PIN %s Estado %s Hora " % (pir_sensor, current_state) + str(datetime.datetime.now()))
            return 1
        else:
            #print("Esperando movimiento, PIN %s Estado %s " % (pir_sensor, current_state))
            return 0

    def limpiar(self):
        GPIO.cleanup()
