## Rclone

sudo apt-get install rclone
cd /home/pi/Desktop/raspberry/video-cloud-motion/
mkdir .config
cd .config
mkdir rclone
cd rclone
touch rclone.conf
chmod 0600 -R rclone.conf
nano rclone.conf
cd ../../
cp -r .config $HOME/

rclone config

rclone ls --max-depth 1 gdrive:

cd ~
mkdir -p mnt/gdrive
rclone mount gdrive: $HOME/mnt/gdrive

mkdir -p $HOME/Desktop/gdrive
rclone mount gdrive:raspberrypi $HOME/Desktop/gdrive
cd $HOME/Desktop/gdrive

Fuente:
https://medium.com/@artur.klauser/mounting-google-drive-on-raspberry-pi-f5002c7095c2
