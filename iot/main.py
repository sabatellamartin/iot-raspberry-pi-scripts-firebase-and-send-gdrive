#!/usr/bin/python
# -*- coding: utf-8 -*-
# autor: Martin Sabatella
# Octubre de 2020
# email: sabatellamartin@gmail.com

#import sys
#from time import sleep
import signal
#from gpiozero import LED, Button
from threading import Thread

# RPi GPIO
import RPi.GPIO as GPIO
import time
import datetime

# Firebase
import firebase_admin # Importo firebase admin
from firebase_admin import credentials # Credenciales de firebase
from firebase_admin import firestore # Comunicacion con firestore

#LED = LED(17)
#BUTTON = Button(27)

PATH_CRED = 'iotrpi-firebase-key.json' # Clave privada para firebase en python

REF_MOVIMIENTOS = 'movimientos' # Coleccion de movimientos

#REF_HOME = 'home'
#REF_LUCES = 'luces'
#REF_BOTONES = 'botones'
#REF_LUZ_SALA = 'luz_sala'
#REF_PULSADOR_A = 'pulsador_a'

class IOT():

    def __init__(self):
        cred = credentials.Certificate(PATH_CRED)
        firebase_admin.initialize_app(cred)

        db = firestore.client()

        self.refMovimientos = db.collection(REF_MOVIMIENTOS)

        #self.refHome = db.reference(REF_HOME)

        #self.estructuraInicialDB() # solo ejecutar la primera vez

        #self.refLuces = self.refHome.child(REF_LUCES)
        #self.refLuzSala = self.refLuces.child(REF_LUZ_SALA)

        #self.refBotones = self.refHome.child(REF_BOTONES)
        #self.refPulsadorA = self.refBotones.child(REF_PULSADOR_A)

#    def estructuraInicialDB(self):
#        self.refHome.set({
#            'luces': {
#                'luz_sala':True,
#                'luz_cocina':True
#            },
#            'botones':{
#                'pulsador_a':True,
#                'pulsador_b':True
#            }
#        })

#    def ledControlGPIO(self, estado):
#        if estado:
#            LED.on()
#            print('LED ON')
#        else:
#            LED.off()
#            print('LED OFF')
    def monitorMovimiento(self):
        # GPIO pin
        pir_sensor = 17
        # Initialze GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pir_sensor, GPIO.IN)
        current_state = 0
        try:
            while True:
                time.sleep(0.1)
                current_state = GPIO.input(pir_sensor)
                if current_state == 1:
                    print("Motion detected, PIN %s State %s at " % (pir_sensor, current_state) + str(datetime.datetime.now()))
                    self.guardaMovimiento(pir_sensor, 1, datetime.datetime.now())
                else:
                    print("Wait motion, PIN %s State %s " % (pir_sensor, current_state))
                time.sleep(1)
        except KeyboardInterrupt:
            pass
        finally:
            GPIO.cleanup()

    def guardaMovimiento(self, pin, estado, timestamp):
        self.refMovimientos.document().set({
            u'timestamp': timestamp,
            u'estado': estado,
            u'pin': pin
        })


#    def lucesStart(self):

#        E, i = [], 0

#        estado_anterior = self.refLuzSala.get()
#        self.ledControlGPIO(estado_anterior)

#        E.append(estado_anterior)

#        while True:
#          estado_actual = self.refLuzSala.get()
#          E.append(estado_actual)

#          if E[i] != E[-1]:
#              self.ledControlGPIO(estado_actual)

#          del E[0]
#          i = i + i
#          sleep(0.4)

#    def pulsador_on(self):
#        print('Pulsador On')
#        self.refPulsadorA.set(True)

#    def pulsador_off(self):
#        print('Pulsador Off')
#        self.refPulsadorA.set(False)

#    def botonesStart(self):
#        print('Start btn !')
#        BUTTON.when_pressed = self.pulsador_on
#        BUTTON.when_released = self.pulsador_off


print ('START !')
iot = IOT()

subproceso_movimiento = Thread(target=iot.monitorMovimiento)
subproceso_movimiento.daemon = True
subproceso_movimiento.start()

#subproceso_led = Thread(target=iot.lucesStart)
#subproceso_led.daemon = True
#subproceso_led.start()

#subproceso_btn = Thread(target=iot.botonesStart)
#subproceso_btn.daemon = True
#subproceso_btn.start()
signal.pause()
