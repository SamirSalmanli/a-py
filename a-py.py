import os
import time
import colorama

def menugoster():
    baslat = colorama.init()
    print(colorama.Fore.LIGHTMAGENTA_EX)

    print("""
             _                             _    _        _   
        / /\                          /\ \ /\ \     /\_\ 
       / /  \                        /  \ \\ \ \   / / / 
      / / /\ \                      / /\ \ \\ \ \_/ / /  
     / / /\ \ \        ____        / / /\ \_\\ \___/ /   
    / / /  \ \ \     /\____/\     / / /_/ / / \ \ \_/    
   / / /___/ /\ \    \/____\/    / / /__\/ /   \ \ \     
  / / /_____/ /\ \              / / /_____/     \ \ \    
 / /_________/\ \ \            / / /             \ \ \   
/ / /_       __\ \_\          / / /               \ \_\  
\_\___\     /____/_/          \/_/                 \/_/  

coder : SamirSalmanli
Github : SamirSalmanli
Instagram : @samirr_py
    
""")
    print(colorama.Fore.BLUE)
    print("""
[1]Termuxu Yenile     [5]Seeker
[2]nmap               [6]Ngrok
[3]metasploit         [7]Zphisher
[4]Sqlmap             [8]Tbomb
[5]MaskPhish          

[11]A-PY yenile 

[10]exit

    """)




def yukle():
    menugoster()

    while True:
        try:
            daxil = int(input("Seciminiz : "))

            while daxil < 1 or daxil > 11:
                daxil = int(input("Yeniden secin ! : "))



            break
        except ValueError:
            print(colorama.Fore.RED)
            print("Yanlis isi secdiniz tekrar secin")

    if daxil == 1: #Termuxu yeniliyir ve lazimi paketleri yukluyur
        print(colorama.Fore.YELLOW)
        print("1 ci is basliyir ........")
        print("Termux yenilenir ve lazimi paketler git,python,ruby ve s yuklenir........")
        time.sleep(1)
        os.system("apt update -y")
        time.sleep(0.5)
        os.system("apt upgrade -y")
        time.sleep(0.5)
        os.system("pkg update && pkg upgrade -y")
        time.sleep(0.5)
        os.system("pkg install git -y")
        time.sleep(0.5)
        os.system("pkg install python python2 -y ")
        time.sleep(0.5)
        os.system("pkg install wget -y")
        time.sleep(0.5)
        os.system("pkg install php -y")
        time.sleep(0.5)
        os.system("pkg install curl -y")
        time.sleep(0.5)
        os.system("pkg install ruby -y")
        time.sleep(0.5)
        os.system("pkg install pip pip2 -y")
        time.sleep(0.5)
        os.system("pkg install clang -y")
        time.sleep(0.5)
        os.system("pkg install vim -y")
        time.sleep(0.5)
        os.system("pkg install proot -y")
        time.sleep(0.5)
        os.system("pkg install perl -y")
        time.sleep(0.5)
        os.system("apt update")
        time.sleep(0.5)
        os.system("apt upgrade")
        time.sleep(0.5)
        os.system("clear")
        time.sleep(0.5)
        print(colorama.Fore.RESET)
        os.system("cd a-py")
        os.system("python a-py.py")


    elif daxil == 2: #Nmap yuklenir
        print(colorama.Fore.YELLOW)
        print("2 ci is basliyir ! NMAP yuklenir .....")
        time.sleep(0.5)
        os.system("pkg install nmap -y")
        time.sleep(0.5)
        print("Nmap yuklendi ... ")
        time.sleep(2)
        os.system("clear")
        print(colorama.Fore.RESET)
        os.system("cd $HOME")
        os.system("cd a-py")
        os.system("python a-py.py")


    elif daxil == 3: #Metasploit yuklenir
        print(colorama.Fore.YELLOW)
        print("3 ci is basliyir ! METASPLOiT yuklenir .....")
        time.sleep(0.5)
        os.system("pkg update && pkg upgrade -y")
        time.sleep(0.5)
        os.system("pkg install wget curl openssh git -y")
        time.sleep(0.5)
        os.system("apt install ncurses-utils")
        time.sleep(0.5)
        os.system("git clone https://github.com/OnlineHacKing/Metasploit_Termux && cd Metasploit_Termux && chmod +x metasploit.sh && bash metasploit.sh")
        time.sleep(0.5)
        print(colorama.Fore.GREEN, "Metasploit Yuklendi !")
        time.sleep(2)
        os.system("cd $HOME")
        os.system("clear")
        print(colorama.Fore.RESET)
        os.system("cd a-py")
        os.system("python a-py.py")



    elif daxil == 4: #sqlmap yukluyur
        print(colorama.Fore.YELLOW)
        print("4 cu is basliyir ! SQLMAP yuklenir .....")
        os.system("git clone https://github.com/sqlmapproject/sqlmap.git")
        time.sleep(0.5)
        print("SQLMAP yuklendi !")
        time.sleep(2)
        os.system("cd $HOME")
        os.system("clear")
        time.sleep(0.5)
        print(colorama.Fore.RESET)
        os.system("cd a-py")
        os.system("python a-py.py")



    elif daxil == 5:#SEeker yukluyur
        print(colorama.Fore.YELLOW)
        print("5 ci is basliyir SEEKER yuklenir ......")
        time.sleep(0.5)
        os.system("git clone https://github.com/thewhiteh4t/seeker")
        time.sleep(0.5)
        os.system("cd seeker")
        time.sleep(0.5)
        os.system("bash termux_install.sh")
        print("seeker yuklendi ! ........")
        time.sleep(2)
        os.system("cd $HOME")
        os.system("clear")
        print(colorama.Fore.RESET)
        os.system("cd a-py")
        os.system("python a-py.py")







    elif daxil == 6:#Ngrok kocurur !
        print(colorama.Fore.YELLOW)
        print("6 ci is basliyir NGROK yuklenir .........")
        time.sleep(0.5)
        os.system("git clone https://github.com/tchelospy/termux-ngrok.git")
        time.sleep(0.5)
        os.system("cd termux-ngrok")
        time.sleep(0.5)
        os.system("chmod +x termux-ngrok.sh")
        time.sleep(0.5)
        os.system("bash termux-ngrok.sh")
        print("NGROk yuklendi ........")
        time.sleep(2)
        os.system("cd $HOME")
        os.system("clear")
        print(colorama.Fore.RESET)
        os.system("cd a-py")
        os.system("python a-py.py")

    elif daxil == 7:#Zphisher
        print(colorama.Fore.YELLOW)
        print("7 ci is basliyir Zphisher yuklenir .....")
        time.sleep(0.8)
        os.system("git clone https://github.com/htr-tech/zphisher")
        print("Zphisher yuklendi ..........")
        time.sleep(2)
        os.system("clear")
        print(colorama.Fore.RESET)
        os.system("cd a-py")
        os.system("python a-py.py")

    elif daxil == 8:#Tbomb
        print(colorama.Fore.YELLOW)
        print("8 ci is basliyir Tbomb yuklenir ...... ")
        time.sleep(0.8)
        os.system("git clone https://github.com/SamirSalmanli/tbombforazerbaijan")
        time.sleep(0.5)
        os.system("cd tbombforazerbaijan")
        os.system("pip install -r qurulum.txt")
        print("Tbomb yuklendi ........")
        time.sleep(2)
        os.system("cd $HOME")
        print(colorama.Fore.RESET)
        os.system("cd a-py")
        os.system("clear")
        os.system("python a-py.py")




    elif daxil == 11 :
        print(colorama.Fore.YELLOW)
        print("A-PY yenilenir ........")
        os.system("git clone https://github.com/SamirSalmanli/a-py")
        os.system("clear")
        print(colorama.Fore.RESET)
        os.system("cd a-py")
        os.system("python a-py.py")


    elif daxil == 10:
        exit()

yukle()

