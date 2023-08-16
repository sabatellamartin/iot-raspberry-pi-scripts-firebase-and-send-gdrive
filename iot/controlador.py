import signal
from threading import Thread

import time
import datetime

from dispositivos.camara import Camara
from dispositivos.motor import Motor
from dispositivos.movimiento import Movimiento
from service.datos import Datos

class Controlador():

    def __init__(self):
        self.movimiento = Movimiento()
        self.camara = Camara()
        self.motor = Motor()
        self.datos = Datos()

    def monitorMovimiento(self):
        while True:
            time.sleep(0.1)
            current_state = self.movimiento.sensarMovimiento()
            if current_state == 1:
                print("Movimiento detectado " + str(datetime.datetime.now()))
                self.motor.avanzar(1, 256)
                self.motor.retroceder(1, 256)
                self.camara.capturarImagen()
                self.camara.capturarVideo()
                self.camara.capturarSecuencia()
            else:
                print("Esperando movimiento")
            time.sleep(1)
        self.movimiento.limpiar()

    def monitorMotor(self):
        E, i = [], 0
        estado_anterior = self.datos.obtenerDispositivos()['motor']
        self.motor.ejecutarEstado(estado_anterior)
        E.append(estado_anterior['activo'])
        while True:
            estado_actual = self.datos.obtenerDispositivos()['motor']
            E.append(estado_actual['activo'])
            if E[i] != E[-1]:
                self.motor.ejecutarEstado(estado_actual)
            del E[0]
            i = i + i
            time.sleep(0.4)


print ('START !')
controlador = Controlador()

subproceso_movimiento = Thread(target=controlador.monitorMovimiento)
subproceso_movimiento.daemon = True
subproceso_movimiento.start()

subproceso_motor = Thread(target=controlador.monitorMotor)
subproceso_motor.daemon = True
subproceso_motor.start()

signal.pause()
