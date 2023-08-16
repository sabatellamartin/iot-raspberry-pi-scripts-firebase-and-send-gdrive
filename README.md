# IOT Raspberry scripts and firebase connection to remote control

Internet of thinks (IoT) proyect using Raspberry PI Model B, camera night vision HD 1080p, 7 inches touch-screen and ultronics kit.

In this repository you will find scripts in Python to control some sensors and actuators, as well as examples to give instructions to the raspberry remotely using Firebase.

It also has a configuration to send the video captures to Google Drive to be able to access them.

## Prepare Raspberry PI

Update repositories
sudo apt-get update

Install python 3.9 (In raspbian jessie needs compile)
sudo apt-get install libssl-dev openssl
wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tgz
sudo tar -xzvf Python-3.9.0.tgz
cd Python-3.9.0
./configure
sudo make
sudo make install

sudo apt install python3 idle3

Instalar pip para python3
sudo apt install python3-pip

Instalar python dev tools
sudo apt install python-dev

Instalar python dev tools
sudo pip install firebase-admin

https://firebase.google.com/docs/admin/setup/#python

Instalar gpiozero
sudo apt install python3-gpiozero

https://gpiozero.readthedocs.io/en/stable/installing.html

#### Conection between Firebase and Python

In Firebase navigate to Settings>Service account and select Python

Download private key like firebase-private-key.json

Tutorial Raspberry + Firebase + Python
https://www.youtube.com/watch?v=pcryAtHpvCE


### Capture commands

Take a picture
raspistill -o image.jpg

Capture fifty seconds of video 
raspivid -o video.h1080 -t 5000
raspivid -o vid.h264 -t 5000

Reproduce video
omxplayer video.h1080

Convert video to MP4
sudo apt install gpac
MP4Box -add vid.h264 pivideo.mp4

### Fonts

Temperature humidity sensor DHT11
https://github.com/szazo/DHT11_Python

Motion sensor PIR
https://pimylifeup.com/raspberry-pi-motion-sensor/

Camara commands
https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspivid.md

Programming camera fr capture
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/7
