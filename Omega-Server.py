import os
import time

def Server():
    os.system("clear")
    
    print("""\033[31m

  /$$$$$$                                                   
 /$$__  $$                                                  
| $$  \__/  /$$$$$$   /$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$ 
|  $$$$$$  /$$__  $$ /$$__  $$|  $$  /$$//$$__  $$ /$$__  $$
 \____  $$| $$$$$$$$| $$  \__/ \  $$/$$/| $$$$$$$$| $$  \__/
 /$$  \ $$| $$_____/| $$        \  $$$/ | $$_____/| $$      
|  $$$$$$/|  $$$$$$$| $$         \  $/  |  $$$$$$$| $$      
 \______/  \_______/|__/          \_/    \_______/|__/      
                                                            
           
           
\033[93m[ \033[94m1 \033[93m] Install Web-Server
\033[93m[ \033[94m2 \033[93m] Start Web-Server
\033[93m[ \033[94m3 \033[93m] Shutdown Web-Server
\033[93m[ \033[94m4 \033[93m] Restart Web-Server
\033[93m[ \033[94m5 \033[93m] Edit Web-Server

\033[93m[ \033[94mx \033[93m] Exit
\033[32m
""")
loop = True
while loop:
    Server()
    what = input(">> ")
#------------------------------------------------------------------------------
    if what == "x":
        os.system("clear")
        print(" ")
        print("[ ! ] Exiting...")
        print(" ")
        os.system(exit)
        os.system(exit)
#------------------------------------------------------------------------------
    elif what == "1":
        os.system("clear")
        print(" ")
        print("[ ! ] Installing Web-Server...")
        print(" ")
        time.sleep(4)
        os.system("apt install apache2")
        os.system("clear")
        print(" ")
        print("[ ! ] Web-Server Installed...")
        print(" ")
        time.sleep(4)
#------------------------------------------------------------------------------
    elif what == "2":
        os.system("clear")
        os.system("cd /data/data/com.termux/files/usr/share/apache2/default-site/htdocs")
        os.system("apachectl start")
        os.system("clear")
        print(" ")
        print("[ ! ] Starting Web-Server...")
        print(" ")
        time.sleep(4)
        print(" ")
        print("[ ! ] Web-Server Sucesfully Started!")
        print("[ ! ] 127.0.0.1:8080")
        time.sleep(4)
        os.system("clear")
#------------------------------------------------------------------------------
    elif what == "3":
        os.system("clear")
        os.system("cd /data/data/com.termux/files/usr/share/apache2/default-site/htdocs")
        os.system("pkill -f httpd")
        os.system("clear")
        print(" ")
        print("[ ! ] Shutdowning Web-Server...")
        print(" ")
        time.sleep(4)
        print(" ")
        print("[ ! ] Web-Server Sucesfully Shutdowned!")
        time.sleep(4)
        os.system("clear")
#------------------------------------------------------------------------------
    elif what == "4":
        os.system("clear")
        print(" ")
        print("[ ! ] Restarting Web-Server...")
        print(" ")
        time.sleep(4)
        os.system("cd /data/data/com.termux/files/usr/share/apache2/default-site/htdocs")
        os.system("pkill -f httpd")
        time.sleep(3)
        os.system("cd /data/data/com.termux/files/usr/share/apache2/default-site/htdocs")
        os.system("apachectl start")
        os.system("clear")
        print(" ")
        print("[ ! ] Web-Server Sucesfully Restarted!")
        print(" ")
        time.sleep(4)
#------------------------------------------------------------------------------
    elif what == "5":
        os.system("clear")
        print(" ")
        print("[ ! ] Installing Editing Program...")
        print(" ")
        time.sleep(4)
        os.system("apt install micro")
        print(" ")
        print("To Exit CTRL + Q")
        print(" ")
        time.sleep(4)
        os.system("micro /data/data/com.termux/files/usr/share/apache2/default-site/htdocs/index.html")
        os.system("clear")
        time.sleep(4)
