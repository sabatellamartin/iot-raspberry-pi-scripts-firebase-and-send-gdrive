import RPi.GPIO as GPIO
import time

coil_A_1_pin = 17 # azul
coil_A_2_pin = 22 # violeta
coil_B_1_pin = 23 # amarillo
coil_B_2_pin = 24 # naranja
enable_pin = coil_A_1_pin

StepCount = 8
Seq = range(0, StepCount)
Seq[0] = [1,0,0,0]
Seq[1] = [1,1,0,0]
Seq[2] = [0,1,0,0]
Seq[3] = [0,1,1,0]
Seq[4] = [0,0,1,0]
Seq[5] = [0,0,1,1]
Seq[6] = [0,0,0,1]
Seq[7] = [1,0,0,1]

class Motor():

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(enable_pin, GPIO.OUT)
        GPIO.setup(coil_A_1_pin, GPIO.OUT)
        GPIO.setup(coil_A_2_pin, GPIO.OUT)
        GPIO.setup(coil_B_1_pin, GPIO.OUT)
        GPIO.setup(coil_B_2_pin, GPIO.OUT)
        GPIO.output(enable_pin, 1)

        #delay = raw_input("Time Delay (ms)?")
        ## 512 pasos es una vuelta completa
        #steps = raw_input("How many steps forward? ")
        #forward(int(delay) / 1000.0, int(steps))
        #steps = raw_input("How many steps backwards? ")
        #backwards(int(delay) / 1000.0, int(steps))

    def setStep(self, w1, w2, w3, w4):
        GPIO.output(coil_A_1_pin, w1)
        GPIO.output(coil_A_2_pin, w2)
        GPIO.output(coil_B_1_pin, w3)
        GPIO.output(coil_B_2_pin, w4)

    def avanzar(self, delay, steps):
        delay = int(delay) / 1000.0
        for i in range(steps):
            for j in range(StepCount):
                self.setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
                time.sleep(delay)

    def retroceder(self, delay, steps):
        delay = int(delay) / 1000.0
        for i in range(steps):
            for j in reversed(range(StepCount)):
                self.setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
                time.sleep(delay)

    def ejecutarEstado(self, motor):
        if motor['activo']:
            if motor['sentido'] == u'horario':
                self.avanzar(motor['tiempo'], motor['pasos'])
            else:
                self.retroceder(motor['tiempo'], motor['pasos'])
