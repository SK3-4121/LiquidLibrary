####################################
######### Made By Max B ###########
############ V : 1.1 #############

Version = "1.1"

import os
import wget
import time
import socket
import requests
import threading
import colorama; colorama.init; Fore = colorama.Fore; RESET = Fore.RESET

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
    c1,c2,c3,c4 = False, False, False, False
    def ck(p):
        return os.path.exists(str(p))
    if ck("Cache"):
        c1 = True
    if ck("Images"):
        c2 = True
    if ck("Scripts"):
        c3 = True
    if ck("Scripts/Settings"):
        c4 = True
    if c1 and c2 and c3 and c4 == True:
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
    Local_IP = socket.gethostbyname('localhost')
    port = 6969 # 7563
    def start_se():
        mount = input("[•]: What directory: ")
        if str(mount) == "":
            mount = "/"
        python_command = f"cd {str(mount)} && python3 -m http.server {str(port)}"
        print(Fore.GREEN + "[+]: Your host link is > http://" + str(Local_IP) + ":" + str(port) + Fore.RESET)
        print(Fore.YELLOW + "~~~~~~~~~~~~~~~~~~~~~~~~~~~ LOGS ~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        os.system(python_command)
        print(RESET)
    HOST_Thread = threading.Thread(target=start_se)
    HOST_Thread.start()

def Loader():
    c1,c2 = False, False
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
        colur("[+]: Certifcation success")
        start_server()
        time.sleep(5)
        test_input = input("[•]: Upload file?")
        outp = input("[•]: New Directory: ")
        wget.download(str(test_input), str(outp))
    else:
        colur("[-]: Certifcation failed auto closing")
        os.close()

def __main__():
    colur("[+]: __main__() has started")
    Loader()

if __name__ == "__main__":
    colur("[+]: Script launched | [" + str(get_time()) + "]")
    __main__()
    #try:
    #    __main__()
    #except:
    #    colur("[-]: There was a error running __main__() [-12254]")
    #    print(RESET)
