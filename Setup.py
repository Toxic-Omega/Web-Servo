import os
import time

def Server():
    os.system("clear")
    
    print("""\033[31m
 __      __      ___.               _________                         
/  \    /  \ ____\_ |__            /   _____/ ______________  ______  
\   \/\/   // __ \| __ \   ______  \_____  \_/ __ \_  __ \  \/ /  _ \ 
 \        /\  ___/| \_\ \ /_____/  /        \  ___/|  | \/\   (  <_> )
  \__/\  /  \___  >___  /         /_______  /\___  >__|    \_/ \____/ 
       \/       \/    \/                  \/     \/                   

                     \033[94mCreated By Toxic-Omega


\033[32m[ \033[31m1 \033[32m\033[32m] Install Web-Servo
\033[32m[ \033[31m2 \033[32m] Start Web-Servo
\033[32m[ \033[31m3 \033[32m] Shutdown Web-Servo
\033[32m[ \033[31m4 \033[32m] Restart Web-Servo
\033[32m[ \033[31m5 \033[32m] Edit Web-Servo

\033[32m[ \033[31mx \033[32m] Exit
""")
loop = True
while loop:
    Server()
    what = input(">> ")
#------------------------------------------------------------------------------
    if what == "x":
        os.system("ls")
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Exiting...")
        print(" ")
        exit
        break
#------------------------------------------------------------------------------
    elif what == "1":
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Installing Web-Server...")
        print(" ")
        time.sleep(4)
        os.system("apt install apache2")
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Web-Server Installed...")
        print(" ")
        time.sleep(4)
#------------------------------------------------------------------------------
    elif what == "2":
        os.system("clear")
        os.system("cd /data/data/com.termux/files/usr/share/apache2/default-site/htdocs")
        os.system("apachectl start")
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Starting Web-Server...")
        print(" ")
        time.sleep(4)
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Web-Server Sucesfully Started!")
        print("\033[32m[\033[31m*\033[32m] 127.0.0.1:8080")
        time.sleep(4)
        os.system("clear")
#------------------------------------------------------------------------------
    elif what == "3":
        os.system("clear")
        os.system("cd /data/data/com.termux/files/usr/share/apache2/default-site/htdocs")
        os.system("pkill -f httpd")
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Shutdowning Web-Server...")
        print(" ")
        time.sleep(4)
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Web-Server Sucesfully Shutdowned!")
        time.sleep(4)
        os.system("clear")
#------------------------------------------------------------------------------
    elif what == "4":
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Restarting Web-Server...")
        print(" ")
        time.sleep(4)
        os.system("cd /data/data/com.termux/files/usr/share/apache2/default-site/htdocs")
        os.system("pkill -f httpd")
        time.sleep(3)
        os.system("cd /data/data/com.termux/files/usr/share/apache2/default-site/htdocs")
        os.system("apachectl start")
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Web-Server Sucesfully Restarted!")
        print(" ")
        time.sleep(4)
#------------------------------------------------------------------------------
    elif what == "5":
        os.system("clear")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] Installing Editing Program...")
        print(" ")
        time.sleep(4)
        os.system("apt install micro")
        print(" ")
        print("\033[32m[\033[31m*\033[32m] To Exit CTRL + Q")
        print(" ")
        time.sleep(4)
        os.system("micro /data/data/com.termux/files/usr/share/apache2/default-site/htdocs/index.html")
        os.system("clear")
        time.sleep(4)
