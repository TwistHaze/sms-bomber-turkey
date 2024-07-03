import os
import colorama
try:
    import httplib
except ImportError:
    import http.client as httplib

colorama.init(convert=True)

def connection():
    conn = httplib.HTTPConnection("www.google.com", timeout=3)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        return False

def display_main_menu():
    if os.name == "nt":
        os.system("title SMS Bomber by TwistHaze")
        os.system("cls")
        
    print(colorama.Fore.CYAN + r"""
                       _________         _________ _______ _________            _______  _______  _______ 
                       \__   __/|\     /|\__   __/(  ____ \\__   __/  |\     /|(  ___  )/ ___   )(  ____ \
                          ) (   | )   ( |   ) (   | (    \/   ) (     | )   ( || (   ) |\/   )  || (    \/
                          | |   | | _ | |   | |   | (_____    | |     | (___) || (___) |    /   )| (__    
                          | |   | |( )| |   | |   (_____  )   | |     |  ___  ||  ___  |   /   / |  __)   
                          | |   | || || |   | |         ) |   | |     | (   ) || (   ) |  /   /  | (      
                          | |   | () () |___) (___/\____) |   | |     | )   ( || )   ( | /   (_/\| (____/\
                          )_(   (_______)\_______/\_______)   )_(     |/     \||/     \|(_______/(_______/
                              Halklar hükümetlerinden korkmamalı, hükümetler halktan korkmalı.                                                          
    """)   
    print(colorama.Fore.YELLOW + """
                                                    Contact Me?
                                  Discord: 404wg    -----------    Instagram 404wg
    """)
    print(colorama.Fore.MAGENTA + "[1] SmsBomb Modülü" + colorama.Fore.GREEN + "\n[2] Script Hakkında Bilgi Al")

def display_info():
    if os.name == "nt":
        os.system("cls")
        os.system("title TwistHaze / SmsBomb Modülü Bilgilendirme")
        
    print(colorama.Fore.CYAN + r"""
                       _________         _________ _______ _________            _______  _______  _______ 
                       \__   __/|\     /|\__   __/(  ____ \\__   __/  |\     /|(  ___  )/ ___   )(  ____ \
                          ) (   | )   ( |   ) (   | (    \/   ) (     | )   ( || (   ) |\/   )  || (    \/
                          | |   | | _ | |   | |   | (_____    | |     | (___) || (___) |    /   )| (__    
                          | |   | |( )| |   | |   (_____  )   | |     |  ___  ||  ___  |   /   / |  __)   
                          | |   | || || |   | |         ) |   | |     | (   ) || (   ) |  /   /  | (      
                          | |   | () () |___) (___/\____) |   | |     | )   ( || )   ( | /   (_/\| (____/\
                          )_(   (_______)\_______/\_______)   )_(     |/     \||/     \|(_______/(_______/
                              Halklar hükümetlerinden korkmamalı, hükümetler halktan korkmalı.                                                          
    """)   
    print(colorama.Fore.YELLOW + """
                                                    Contact Me?
                                  Discord: 404wg    -----------    Instagram 404wg
    """)
    print(colorama.Fore.MAGENTA + "   Ben TwistHaze. Bu eğitim amaçlı hazırlanmıştır. Kötüye kullanımlardan TwistHaze sorumlu değildir." + 
          colorama.Fore.GREEN + "\n\n   Sistemi durdurmak için CTRL+SHIFT+C kombinasyonunu kullanınız. Durmazsa birkaç defa tekrarlayın.\n")

if not connection():
    if os.name == "nt":
        os.system("cls")
    print(colorama.Fore.RED + "Internet bağlantını kontrol et" + colorama.Fore.WHITE)
    os._exit(1)

while True:
    display_main_menu()
    moduleinput = int(input(colorama.Fore.RESET + "\n[Twist Haze] SMS Bomber İçin 1 Yaz > "))
    
    if moduleinput == 1:
        if os.name == "nt":
            os.system("title TwistHaze / SmsBomb Modülü")
            os.system("cls")
        print(colorama.Fore.MAGENTA + "[1] SMSBomberTR(Proxysiz, Türkiye)" + colorama.Fore.GREEN + "\n[2] Ana Menüye Dön")
        smsinput = int(input(colorama.Fore.RESET + "\n[Twist Haze] Modül Seç > "))
        
        if smsinput == 1:
            if os.name == "nt":
                os.system("cls")
            from Modules.SMS.smsbomber.smsbomber import *
        elif smsinput == 2:
            continue
    
    elif moduleinput == 2:
        display_info()
        
        # Kullanıcı tekrar enter'a basarsa başlangıca dönecek
        input(colorama.Fore.RESET + "\n[Twist Haze] Başlangıca dönmek için enter'a basın... ")
