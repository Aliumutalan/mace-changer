import random
import subprocess
def menu():
    menu = """
    What do you want??
    
    1 ) Change mac
    2 ) Learn İnterface
    3 ) EXİT
    
    """
    print(menu)
    choise = int(input("Whats your choise??"))
    if choise == 1 :
        changemac()
    elif choise == 2:
        learninterface()
    elif choise == 3:
        exit()
    else :
        print("whats your problem bro??")
        menu()

def changemac():
    def defaultchange():
        maclist=["88:34:fd:40:b0:73","05:cc:8d:46:08:f6","a3:4c:0d:98:c2:65","dd:8b:f5:13:95:6b","bd:b3:99:35:ed:06","91:19:8b:8e:99:5a","26:79:21:9f:a5:11","73:41:72:92:96:b5","54:5c:4e:74:26:84","0b:94:db:17:34:a9","ce:9a:c4:88:b0:e3","5f:94:65:95:49:76","94:cf:73:79:ed:e4","aa:34:9b:3d:a8:96"]
        iterface = input("whats your interface:   ")
        subprocess.call(["ifconfig", iterface, "down"])
        subprocess.call(["ifconfig", iterface, "hw", "ether", random.choice(maclist)])
        subprocess.call(["ifconfig", iterface, "up"])
        print("mission completed")
        print("if you want go menu 0")
        back = int(input())
        if back == 0:
            menu()
    def manuelchange():
        iterface = input("whats your interface:   ")
        mymac = input("whats your mac:   ")
        subprocess.call(["ifconfig",iterface,"down"])
        subprocess.call(["ifconfig",iterface,"hw","ether",mymac])
        subprocess.call(["ifconfig",iterface,"up"])
        print("mission completed")
        print("if you want go menu 0")
        back = int(input())
        if back == 0:
            menu()
    menu2 = """
    How do you want change mac
    1 )Default change
    2 )I change
    """
    print(menu2)
    hextex = int(input("choise:   "))
    if hextex == 1 :
        defaultchange()
    elif hextex == 2:
        manuelchange()
    else:
        print("whats your problem amigo???")
        menu()
def learninterface():
    subprocess.call(["clear"])
    subprocess.call(["ifconfig"])
    print("Going for menu 0")
    back= int(input())
    if back == 0 :
        menu()
menu()
