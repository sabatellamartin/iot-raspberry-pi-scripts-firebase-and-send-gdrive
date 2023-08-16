#!/usr/bin/python
# -*- coding: utf-8 -*-
# autor: Martin Sabatella
# Octubre de 2020
# email: sabatellamartin@gmail.com

import signal
from threading import Thread

# RPi GPIO
import RPi.GPIO as GPIO
import time
import datetime

# Firebase
import firebase_admin # Importo firebase admin
from firebase_admin import credentials # Credenciales de firebase
from firebase_admin import firestore # Comunicacion con firestore

PATH_CRED = 'iotrpi-firebase-key.json' # Clave privada para firebase en python

REF_MOVIMIENTOS = 'movimientos' # Coleccion de movimientos

class IOT():

    def __init__(self):
        cred = credentials.Certificate(PATH_CRED)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        self.refMovimientos = db.collection(REF_MOVIMIENTOS)

    def monitorMovimiento(self):
        pir_sensor = 25 # GPIO pin
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

print ('START !')
iot = IOT()

subproceso_movimiento = Thread(target=iot.monitorMovimiento)
subproceso_movimiento.daemon = True
subproceso_movimiento.start()

signal.pause()
