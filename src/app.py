####################################
######### Made By Max B ###########
############ V : 1.1 #############

Version = "1.1"

import os
import time
import socket
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

def start_server():
    os.system("SSHswitch on")
    print(Fore.GREEN + "[+]: Starting LOCALHOST SFTP SERVER" + Fore.RESET)
    print(Fore.YELLOW + "[•]: If something shows in the logs thats not good")
    print(Fore.YELLOW + "~~~~~~~~~~~~~~~~~~~~~~~~~~~ LOGS ~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def Loader():
    c1,c2 = True, False
    if check_Directorys() == True:
        colur("[+]: All files found!")
        c2 = True
    else:
        colur("[-]: Failed to find all files")
    if c1 and c2 == True:
        colur("[+]: Certifcation success")
        start_server()
        time.sleep(5)
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
