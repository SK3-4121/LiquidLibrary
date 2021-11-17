echo ##############################
echo ######### Installer #########
echo ########### V1.1 ###########

apt update
apt upgrade

apt install python3 wget git

git clone https://github.com/SK3-4121/LiquidLibrary.git

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
./run.sh
