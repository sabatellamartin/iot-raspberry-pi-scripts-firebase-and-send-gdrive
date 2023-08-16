from picamera import PiCamera
from time import sleep

BASE_PATH = '/home/pi/Desktop/'

class Camara():

    def __init__(self):
        self.camera = PiCamera()

    def capturarVideo(self):
        self.camera.start_preview()
        self.camera.start_recording(BASE_PATH+'video.h264')
        sleep(5)
        self.camera.stop_recording()
        self.camera.stop_preview()

    def capturarImagen(self):
        self.camera.start_preview()
        #self.camera.rotation = 180
        sleep(2)
        self.camera.capture(BASE_PATH+'image.jpg')
        self.camera.stop_preview()

    def capturarSecuencia(self):
        self.camera.start_preview()
        for i in range(5):
            sleep(2)
            self.camera.capture(BASE_PATH+'image%s.jpg' % i)
        self.camera.stop_preview()
