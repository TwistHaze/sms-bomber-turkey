import os,colorama
try:
    import httplib
except:
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

if (connection() == False):
	if(os.name == "nt"):
		os.system("cls")
	print(colorama.Fore.RED + "Internet bağlantını kontrol et" + colorama.Fore.WHITE)
	os._exit(1)


if (os.name =="nt"):
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
    print(colorama.Fore.YELLOW + '                                              Contact Me?')
    print(colorama.Fore.YELLOW + '                            Discord: 404wg    -----------    Instagram 404wg     ')
    print("")
    print("")
print(colorama.Fore.MAGENTA + "[1] SmsBomb Modülü" + colorama.Fore.GREEN + "\n[2] Script Hakkında Bilgi Al")
moduleinput = int(input(colorama.Fore.RESET + "\n[Twist Haze] SMS Bomber İçin 1 Yaz > "))

#SMS Modules
if moduleinput == 1:
    if (os.name =="nt"):
        os.system("title TwistHaze / SmsBomb Modülü")
        os.system("cls")
    print(colorama.Fore.MAGENTA + "[1] SMSBomberTR(Proxysiz, Türkiye)")
    smsinput = int(input(colorama.Fore.RESET + "\n[TwistHaze] Modül Seç > "))  
#SMS Inputs    
    if smsinput == 1:
        if (os.name =="nt"):
            os.system("cls")
        from Modules.SMS.smsbomber.smsbomber import *    

  #Bilgilendirme 2
if moduleinput == 2:
    if (os.name =="nt"):
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
    print(colorama.Fore.YELLOW + '                                              Contact Me?')
    print(colorama.Fore.YELLOW + '                            Discord: 404wg    -----------    Instagram 404wg     ')
    print("")
    print("")
    print("")
    print("")
    print(colorama.Fore.MAGENTA + "   Ben TwistHaze. Bu eğitim amaçlı hazırlanmıştır. Kötüye kullanımlardan TwistHaze sorumlu değildir." + colorama.Fore.GREEN + "\n\n   Sistemi durdurmak için CTRL+SHIFT+C kombinasyonunu kullanınız. Durmazsa birkaç defa tekrarlayın.\n\n\n\n\n\n\n\n")
