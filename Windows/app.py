####################################
######### Made By Max B ###########
############ V : 1.2 #############

Lip = "192.168.1.119"
Port = 7563
Version = "1.2"
debug = False

import os
import json
import time
import string
import socket
import random
import requests
import threading
import colorama; colorama.init; Fore = colorama.Fore; RESET = Fore.RESET

from pyqrcode import QRCode
from tkinter import *
from PIL import ImageTk, Image

Pc = ""
Phone = ""

def finish_json():
    global PC, Phone
    if Lip != "":
        with open('config.json') as f:
            config = json.load(f)
            Pc = config["PC"]
            Phone = config["Phone"]

        dictionary = {
            "Version": "1.2",
            "PC": Lip,
            "Phone": Phone,
            "PHP": "C:/Users/Shx32/Desktop/LiUpload/Ice/php-8.0"
        }

        with open("config.json", "w") as outfile:
            json.dump(dictionary, outfile)

finish_json()

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

dir = 'Images'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

def get_time():
    return str(time.asctime(time.localtime(time.time())))

def colur(p):
    try:
        if str(p[0:4]) == "[-]:" or str(p[0:4]) == "":
            print(Fore.RED + str(p) + RESET)
        if str(p[0:4]) == "[+]:": 
            print(Fore.GREEN + str(p) + RESET)
        if str(p[0:4]) == "[•]:": 
            print(Fore.YELLOW + str(p) + RESET)
    except:
        print("[-]: Failed to print Fore [-55414]")

def check_Directorys():
    c1 = False
    def ck(p):
        return os.path.exists(str(p))
    if ck("Images"):
        c1 = True
    if c1 == True:
        return True

def Internet_Connection():
    request = requests.Session()
    try:
        request.post("https://google.com", timeout=5)
        return True
    except requests.Timeout:
        pass
    except requests.ConnectionError:
        return False

def start_server():
    Local_IP = socket.gethostbyname(socket.gethostname())
    def start_se():
        mount = "Scaner/" # here is . and one out is ..
        python_command = f"cd {str(mount)} && C:/Users/Shx32/Desktop/LiUpload/Ice/php-8.0/php.exe -S {Lip}:{Port}"
        #print(Fore.GREEN + "[+]: Your host link is > http://" + Local_IP + ":" + str(Port) + Fore.RESET)
        print(Fore.YELLOW + "~~~~~~~~~~~~~~~~~~~~~~~~~~~ LOGS ~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        os.system(python_command)
        print(RESET)
        finish_json()
    HOST_Thread = threading.Thread(target=start_se)
    HOST_Thread.start()

def Loader():
    c1 = False
    c2 = False
    if Internet_Connection() == True:
        colur("[+]: Connected to the internet")
        c1 = True
    else:
        colur("[-]: Not connected to internet [-51556]")
    if check_Directorys() == True:
        colur("[+]: All files found!")
        c2 = True
    else:
        colur("[-]: Failed to find all files")
    if c1 and c2 == True:
        return True

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def Generate_QRC(url):
    import qrcode
    input_data = str(url) 
    qr = qrcode.QRCode(
        version=5,
        box_size=8,
        border=1
    )
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='#fffff', back_color='#5662f6')
    st = id_generator()
    img.save("Images/" + str(st + ".png"))
    start_server()
    os.system("cd Images && " + str(st + ".png"))

def __main__():
    colur("[+]: __main__() has started")
    if Loader() == True:
        print(colorama.Fore.GREEN + "[+]: Successfully hosted the URL And QRC!" + colorama.Fore.RESET)
        Generate_QRC(f"http://{Lip}:{Port}/")
        #finish_json()

if __name__ == "__main__":
    colur("[+]: Script launched | [" + str(get_time()) + "]")
    if debug == False:
        try:
            __main__()
        except:
            colur("[-]: There was a error running __main__() [-12254]")
            print(RESET)
            finish_json()
    else:
        __main__()
        finish_json()
