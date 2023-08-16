from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
#camera.rotation = 180
#sleep(2)
#camera.capture('/home/pi/Desktop/image.jpg')

for i in range(5):
    sleep(2)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)

camera.stop_preview()
