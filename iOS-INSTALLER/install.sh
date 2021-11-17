#!/bin/sh
echo ##############################
echo ######### Installer #########
echo ########### V1.1 ###########

apt update
#apt upgrade

cd /var/mobile/Downloads

apt install python3 wget git

git clone https://github.com/SK3-4121/LiquidLibrary.git

cd LiquidLibrary

curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
python3 get-pip.py

/usr/bin/python3 -m pip install --upgrade pip

pip install colorama requests

rm -f -r get-pip.py

mkdir Cache
mkdir Images
mkdir Scripts
mkdir Scripts/Settings

chmod 777 LiquidLibrary
cd LiquidLibrary
chmod +x run.sh

echo ^ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ LOGS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ^
echo Run "./run.sh" to run the application

python3
import os
a = input(str("Click Return/Enter to respring"))
os.system("sbreload")
