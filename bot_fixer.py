import os, sys, uuid, string, random, re
from os import system as sm
try:
    import httpx, requests
    from rich import print as rp
    from bs4 import BeautifulSoup as bsoup
    from rich.prompt import Prompt as p1
    from concurrent.futures import ThreadPoolExecutor as ter
except:
    os.system('python3.12 -m pip install rich httpx futures')

def ua():
    major_versions = [300, 321, 326, 330, 340, 350, 360, 370, 380] 
    major_version = random.choice(major_versions)
    minor_version = random.randint(50, 99) if major_version > 350 else random.randint(0, 49)
    patch_version = random.randint(500, 999) if major_version > 350 else random.randint(100, 499)
    
    fbav = f"{major_version}.{minor_version}.0.{patch_version}"
    fbbv = str(random.randint(100000000, 999999999))
    density = random.choice(["1.0", "1.5", "2.0", "2.5", "3.0", "4.0", "5.0", "6.0", "8.0"])

    width = random.choice(["1280", "1366", "1440", "1600", "1920", "2560", "2880", "3200", "3840", "4096", "5120"])
    height = random.choice(["720", "768", "900", "1080", "1440", "1600", "1800", "2160", "2400", "2880", "3200"])

    fblc = random.choice([
        "fr_FR", "en_US", "es_ES", "de_DE", "it_IT", "pt_BR", "zh_CN", "ja_JP", "ko_KR", "ar_AR", "ru_RU", "tr_TR",
        "pl_PL", "nl_NL", "sv_SE", "da_DK", "fi_FI", "no_NO", "cs_CZ", "hu_HU", "el_GR", "ro_RO", "sk_SK", "bg_BG",
        "hr_HR", "sr_RS", "lt_LT", "lv_LV", "et_EE", "ms_MY", "th_TH", "vi_VN", "id_ID", "hi_IN", "bn_BD", "fa_IR", "uk_UA", "he_IL"
    ])
    fbrv = str(random.randint(200000000, 900000000))
    
    fbca = random.choice(["x86", "x86_64", "amd64", "intel64", "arm64", "arm", "armv7", "armv8", "armv7l", "ia64", "ppc", "ppc64", "mips", "mips64", "sparc", "sparc64", "riscv", "riscv64"])
    
    fbpn_values = [
        "com.facebook.katana", 
        "com.facebook.lite", 
        "com.facebook.messenger",
        "com.facebook.web"
    ]
    fbpn = random.choice(fbpn_values)
    
    fbsrv = f"{random.randint(13, 18)}.0"
    fbop = str(random.randint(5, 30))

    hp_laptop_models = [
        "HP Pavilion 15", "HP Envy x360", "HP Spectre x360", 
        "HP EliteBook 840", "HP Omen 15", "HP ProBook 450",
        "HP Chromebook 14", "HP ZBook Studio G7", "HP Stream 14",
        "HP Elite Dragonfly", "HP Envy 13", "HP 15s", "HP EliteBook x360",
        "HP Pro x2", "HP ZBook Fury 15", "HP Envy 17", "HP Spectre Folio",
        "HP Pavilion x360", "HP Chromebook x2", "HP OMEN X 2S", "HP ENVY x2",
        "HP EliteBook 850", "HP ZBook Create G7", "HP Pavilion Gaming 16",
        "HP ENVY 15", "HP Omen X", "HP ZBook 17 G6", "HP Envy x2",
        "HP Omen 17", "HP Pavilion 14", "HP 250 G8", "HP EliteBook 1040",
        "HP Pavilion Gaming 15", "HP Chromebook 11", "HP ProBook 640",
        "HP EliteBook 830", "HP ZBook Power G8", "HP Omen Obelisk",
        "HP Spectre x2", "HP EliteBook 735", "HP Envy x360 15", 
        "HP ProBook 440", "HP Pavilion Aero 13", "HP ZBook Firefly 14",
        "HP Stream 11", "HP EliteBook 845", "HP Chromebook x360 14c",
        "HP ProBook 455", "HP Pavilion 13"
    ]

    dell_laptop_models = [
        "Dell XPS 13", "Dell XPS 15", "Dell Inspiron 15", "Dell Inspiron 13",
        "Dell Latitude 7420", "Dell Latitude 7320", "Dell Vostro 14", "Dell G5 15",
        "Dell Precision 3550", "Dell Alienware M15", "Dell G7 17", "Dell XPS 17",
        "Dell Inspiron 16 Plus", "Dell Latitude 9420", "Dell Precision 5550",
        "Dell Inspiron 14", "Dell Latitude 5520", "Dell Precision 5750", 
        "Dell Alienware X17", "Dell G3 15", "Dell Inspiron 14 5000", 
        "Dell Precision 7750", "Dell Vostro 13", "Dell Alienware Area-51m", 
        "Dell XPS 13 2-in-1", "Dell Latitude 3410", "Dell G15", "Dell Inspiron 7000", 
        "Dell Latitude 5400", "Dell Vostro 15 3000", "Dell Precision 3551",
        "Dell XPS 13 Plus", "Dell Inspiron 13 7000", "Dell Latitude 5430", 
        "Dell Precision 7560", "Dell Alienware m17 R5", "Dell G15 5515", 
        "Dell Inspiron 14 7000", "Dell Latitude 7440", "Dell XPS 15 9520", 
        "Dell G16", "Dell Inspiron 15 5000", "Dell Precision 3570", 
        "Dell Vostro 15 5000", "Dell Alienware x14", "Dell Latitude 7330", 
        "Dell XPS 13 OLED", "Dell Inspiron 16 7000", "Dell Precision 5580", 
        "Dell Alienware x17 R2", "Dell G15 5520", "Dell Inspiron 13 5000", 
        "Dell Latitude 7430", "Dell XPS 17 9720", "Dell Vostro 15 7000"
    ]

    lenovo_laptop_models = [
        "Lenovo ThinkPad X1 Carbon", "Lenovo Yoga Slim 7i", "Lenovo Legion 5",
        "Lenovo IdeaPad 3", "Lenovo Yoga 9i", "Lenovo ThinkBook 14s",
        "Lenovo ThinkPad T14", "Lenovo IdeaPad Flex 5", "Lenovo Yoga C940",
        "Lenovo ThinkPad P15", "Lenovo Legion 7", "Lenovo ThinkPad X13",
        "Lenovo Legion Y740", "Lenovo IdeaPad S540", "Lenovo ThinkPad X1 Extreme",
        "Lenovo ThinkPad L13", "Lenovo Yoga 7i", "Lenovo ThinkPad P1", "Lenovo Legion 5 Pro", 
        "Lenovo IdeaPad Gaming 3", "Lenovo ThinkPad X12 Detachable", "Lenovo Yoga Duet 7i", 
        "Lenovo Legion Slim 7", "Lenovo ThinkPad X280", "Lenovo IdeaPad 5", 
        "Lenovo ThinkBook Plus", "Lenovo ThinkPad L15", "Lenovo Yoga S940", 
        "Lenovo ThinkPad E14", "Lenovo ThinkPad P17", "Lenovo Legion Y530",
        "Lenovo ThinkPad X1 Yoga Gen 6", "Lenovo Yoga 9i 14", "Lenovo Legion 7i", 
        "Lenovo IdeaPad 5 Pro", "Lenovo ThinkBook 15 Gen 3", "Lenovo Yoga 6", 
        "Lenovo ThinkPad X1 Nano", "Lenovo Legion 5i Pro", "Lenovo IdeaPad Flex 5i", 
        "Lenovo ThinkPad L15 Gen 2", "Lenovo Yoga 9i 15", "Lenovo ThinkPad P52", 
        "Lenovo ThinkPad T15", "Lenovo Legion 5 Pro 16", "Lenovo IdeaPad Gaming 3i", 
        "Lenovo ThinkPad X1 Carbon Gen 10", "Lenovo Yoga 7i 14", "Lenovo Legion 5i", 
        "Lenovo IdeaPad 5i Pro", "Lenovo ThinkPad P43s", "Lenovo Yoga C9", 
        "Lenovo ThinkPad X1 Fold", "Lenovo ThinkBook 14 Gen 2", "Lenovo Legion 7i Pro", 
        "Lenovo Yoga 9i 13", "Lenovo IdeaPad Gaming 3 Pro"
    ]

    acer_laptop_models = [
        "Acer Swift 3", "Acer Predator Helios 300", "Acer Aspire 5", "Acer Spin 5",
        "Acer Chromebook 314", "Acer Nitro 5", "Acer TravelMate P6", "Acer ConceptD 7",
        "Acer Enduro N7", "Acer Chromebook Spin 713", "Acer Aspire 7", "Acer Swift 7",
        "Acer TravelMate P2", "Acer Aspire E 15", "Acer Swift X", "Acer Aspire 3", 
        "Acer Spin 3", "Acer Predator Triton 300", "Acer Enduro Urban N3", 
        "Acer ConceptD 3", "Acer Chromebook 514", "Acer Nitro 7", "Acer Aspire S3", 
        "Acer Spin 7", "Acer TravelMate X5", "Acer Enduro T1", "Acer Aspire VX 15", 
        "Acer Swift 5", "Acer TravelMate B3", "Acer Predator Helios 500",
        "Acer Aspire Vero", "Acer Predator Triton 500 SE", "Acer Chromebook 317",
        "Acer Swift Edge", "Acer Aspire 5 A515", "Acer Nitro 16", 
        "Acer Spin 714", "Acer Enduro Urban T3", "Acer TravelMate P4",
        "Acer ConceptD 9", "Acer Chromebook 315", "Acer Aspire 5 Slim",
        "Acer Swift Go", "Acer Predator Helios Neo 16", "Acer Chromebook Vero 514",
        "Acer Aspire 7 Nitro 5", "Acer Predator Helios 700", "Acer Swift 5X", 
        "Acer Aspire 5 Pro", "Acer Nitro 50", "Acer Predator Triton 300 SE",
        "Acer Chromebook 311", "Acer ConceptD 7 Ezel", "Acer Enduro T5", 
        "Acer Swift 3X", "Acer Predator Helios 300 SE", "Acer Aspire 3 A315",
        "Acer Spin 5 Pro", "Acer Nitro 5 AN515", "Acer Chromebook 11 C732",
        "Acer ConceptD 5", "Acer Enduro N3", "Acer Aspire 1", "Acer Swift 3 SF314"
    ]

    asus_laptop_models = [
        "ASUS ZenBook Duo", "ASUS ROG Zephyrus G14", "ASUS VivoBook S15", "ASUS TUF Dash F15",
        "ASUS Chromebook Flip", "ASUS ExpertBook B9", "ASUS ROG Strix G15", "ASUS ZenBook 14",
        "ASUS VivoBook Flip 14", "ASUS ROG Flow X13", "ASUS ProArt StudioBook Pro", "ASUS TUF Gaming A15",
        "ASUS ZenBook Pro Duo", "ASUS VivoBook 15", "ASUS ROG Zephyrus M16", "ASUS ZenBook 13",
        "ASUS Chromebook C425", "ASUS VivoBook S14", "ASUS ZenBook Flip S", "ASUS TUF Gaming F17",
        "ASUS ROG Strix Scar 15", "ASUS VivoBook Ultra K15", "ASUS ZenBook S",
        "ASUS ROG Zephyrus G15", "ASUS VivoBook Pro 14", "ASUS ROG Zephyrus S17", "ASUS ExpertBook P1",
        "ASUS ROG Zephyrus Duo 15", "ASUS VivoBook E14",
        "ASUS ZenBook Flip 13", "ASUS VivoBook K571", "ASUS ExpertBook L1",
        "ASUS ROG Strix Scar 17", "ASUS Chromebook CX9", "ASUS TUF Gaming FX505",
        "ASUS ZenBook UX425", "ASUS ROG Strix G17", "ASUS VivoBook 14",
        "ASUS ProArt StudioBook 16", "ASUS TUF Gaming FX705", "ASUS ZenBook Flip 15",
        "ASUS VivoBook 17", "ASUS ROG Zephyrus G GA502", "ASUS ExpertBook P2",
        "ASUS ROG Strix Hero III", "ASUS ZenBook UX434", "ASUS VivoBook Flip TP470",
        "ASUS ROG Zephyrus Duo SE", "ASUS Chromebook C223", "ASUS VivoBook Ultra 15",
        "ASUS ZenBook 15", "ASUS ROG Flow X16", "ASUS TUF Gaming A17",
        "ASUS VivoBook Flip TP401", "ASUS ROG Zephyrus GX501", "ASUS VivoBook E12",
        "ASUS ZenBook Pro 15", "ASUS ROG Zephyrus S GX701", "ASUS TUF Gaming FX506",
        "ASUS Chromebook Flip C434", "ASUS ZenBook Pro 14", "ASUS VivoBook 13 Slate OLED",
        "ASUS ROG Zephyrus M GU502", "ASUS Chromebook Detachable CM3", "ASUS VivoBook Pro 15",
        "ASUS TUF Dash F17", "ASUS ZenBook Flip UX363", "ASUS ROG Strix Scar III",
        "ASUS VivoBook S14 S433", "ASUS Chromebook Flip C536", "ASUS ROG Zephyrus G15 GA503",
        "ASUS VivoBook Flip TM420", "ASUS ZenBook Pro Duo UX581", "ASUS ExpertBook B1",
        "ASUS VivoBook Flip 12", "ASUS ROG Strix G531", "ASUS ZenBook 14X OLED",
        "ASUS TUF Gaming A15 FA506", "ASUS ZenBook Flip 14 UX463", "ASUS VivoBook 15 X515",
        "ASUS ROG Zephyrus G15 GA502", "ASUS ZenBook S UX393", "ASUS Chromebook Flip C214",
        "ASUS ZenBook Pro Duo 15", "ASUS ExpertBook B3 Flip", "ASUS VivoBook Ultra K14",
        "ASUS ROG Zephyrus Duo 16", "ASUS Chromebook C202", "ASUS TUF Dash FX516",
        "ASUS ZenBook 13 OLED", "ASUS VivoBook S14 M433", "ASUS ZenBook Flip UX461",
        "ASUS ROG Zephyrus GX531", "ASUS VivoBook Ultra A512", "ASUS Chromebook C523",
        "ASUS ZenBook 13 UX325", "ASUS TUF Gaming FX504", "ASUS ZenBook Flip S UX370",
        "ASUS VivoBook Flip TP501", "ASUS ZenBook Flip 14 UM462", "ASUS Chromebook C302",
        "ASUS VivoBook Flip 14 TP412", "ASUS ZenBook Pro Duo UX582", "ASUS VivoBook 15 X512"
    ]
    
    alienware_laptop_models = [
        "Alienware m15 R7", "Alienware x15 R2", "Alienware x17 R2", 
        "Alienware m17 R5", "Alienware Area-51m R2", "Alienware m15 R6", 
        "Alienware m17 R4", "Alienware x17 R1", "Alienware Area-51m", 
        "Alienware 13 R3", "Alienware 17 R5", "Alienware Aurora R11", 
        "Alienware 15 R2", "Alienware 18", "Alienware m15 R5", 
        "Alienware 15 R3", "Alienware Area-51m R1", "Alienware 17 R4",
        "Alienware m15", "Alienware 13 R2", "Alienware x14", "Alienware M11x", 
        "Alienware M14x", "Alienware M17x", "Alienware 17 R3", 
        "Alienware 15 R4", "Alienware 13 R1", "Alienware 18 R1", 
        "Alienware M17", "Alienware Aurora R10", "Alienware Aurora R9"
    ]

    samsung_laptop_models = [
        "Samsung Galaxy Book Pro 360", "Samsung Galaxy Book Flex2 Alpha", 
        "Samsung Galaxy Book Ion", "Samsung Galaxy Book Go", "Samsung Notebook 9 Pro", 
        "Samsung Notebook Odyssey Z", "Samsung Galaxy Book S", "Samsung Notebook 7 Spin", 
        "Samsung Notebook 9 Pen", "Samsung Chromebook Plus V2", 
        "Samsung Galaxy Chromebook 2", "Samsung Notebook 5", "Samsung Galaxy Book Ion2", 
        "Samsung Galaxy Book Flex Alpha", "Samsung ATIV Book 9", "Samsung ATIV Book 4", 
        "Samsung Notebook 9", "Samsung Chromebook 4", "Samsung ATIV Book 8", 
        "Samsung Chromebook Pro", "Samsung Galaxy Chromebook", 
        "Samsung Galaxy Book Flex 15", "Samsung Galaxy Book Pro", "Samsung Chromebook Plus", 
        "Samsung ATIV Book 2", "Samsung Notebook Series 7", "Samsung Notebook Series 9", 
        "Samsung Galaxy Book Flex 13", "Samsung Notebook 7", "Samsung ATIV Smart PC"
    ]

    razer_laptop_models = [
        "Razer Blade 15 Advanced Model", "Razer Blade 14", "Razer Blade Stealth 13", 
        "Razer Blade Pro 17", "Razer Book 13", "Razer Blade 15 Base Model", 
        "Razer Blade 17 Pro", "Razer Blade Stealth 12.5\"", "Razer Blade Studio Edition", 
        "Razer Blade 13 Mercury White", "Razer Blade 13 Quartz Pink", "Razer Blade 15 OLED", 
        "Razer Book 2020 Edition", "Razer Blade 15 Advanced Model 2021", 
        "Razer Blade 15 Base Model 2020", "Razer Blade 17 Pro 2021", 
        "Razer Blade Pro 17 2020", "Razer Blade 15 OLED 2020", 
        "Razer Blade 15 Base Model 2021", "Razer Blade Stealth 2021", 
        "Razer Blade 14 2021", "Razer Blade Pro 2021", "Razer Blade 13 Early 2020", 
        "Razer Blade Stealth 2019", "Razer Blade Stealth 2017", "Razer Blade 2016", 
        "Razer Blade Pro 2017", "Razer Blade 15 Advanced Model 2018", 
        "Razer Blade 15 Base Model 2019", "Razer Blade Stealth 2018"
    ]

    msi_laptop_models = [
        "MSI GE76 Raider", "MSI GS66 Stealth", "MSI Creator Z16", "MSI GP66 Leopard", 
        "MSI Summit E13 Flip Evo", "MSI GS75 Stealth", "MSI GL65 Leopard", 
        "MSI GT76 Titan", "MSI Prestige 14 Evo", "MSI Alpha 15", "MSI Modern 15", 
        "MSI Prestige 15 A10SC", "MSI Bravo 15", "MSI Katana GF66", "MSI Pulse GL66", 
        "MSI GF63 Thin", "MSI WS66", "MSI WE75", "MSI GF65 Thin", "MSI Stealth 15M", 
        "MSI Prestige 15", "MSI WS75", "MSI Modern 14", "MSI GP65 Leopard", 
        "MSI Prestige 14", "MSI GT75 Titan", "MSI GL63", "MSI GV72", 
        "MSI GL72M", "MSI GL62M", "MSI GS63VR"
    ]

    lg_laptop_models = [
        "LG Gram 17", "LG Gram 16 2-in-1", "LG Gram 14", "LG Ultra PC 17", 
        "LG Ultra Gear 17", "LG Gram 15Z90N", "LG Gram 14Z90P", "LG Gram 16Z90P", 
        "LG Gram 13.3\"", "LG Gram Ultra-Light", "LG Gram Ultra Slim", 
        "LG Gram 17Z90P", "LG Gram 14T90N", "LG Ultra-Light 14U70Q", 
        "LG Gram 14T90P", "LG Gram 16T90P", "LG Ultra PC 16", 
        "LG Ultra Gear 15", "LG Gram 15Z90P", "LG Gram 17Z90N", "LG Gram 16T90N", 
        "LG Gram 13Z990", "LG Gram 14Z990", "LG Ultra Gear 16", 
        "LG Gram 15Z980", "LG Gram 17Z980", "LG Gram 15Z990", "LG Ultra-Light 15", 
        "LG Gram 14Z980", "LG Gram 17T90P"
    ]

    brands = {
        "HP": hp_laptop_models,
        "Dell": dell_laptop_models,
        "Lenovo": lenovo_laptop_models,
        "Acer": acer_laptop_models,
        "ASUS": asus_laptop_models,
        "Alienware": alienware_laptop_models,
        "Samsung": samsung_laptop_models,
        "Razer": razer_laptop_models,
        "MSI": msi_laptop_models
    }

    manufacturer = random.choice(list(brands.keys()))
    model = random.choice(brands[manufacturer])

    operating_systems = ["Windows 10", "Windows 11", "Windows 8.1", "Windows 7", "Ubuntu", "Fedora", "Debian", "Linux Mint", "Elementary OS", "Chrome OS", "Pop!_OS", "Red Hat Enterprise Linux", "Linux", "CentOS", "Manjaro Linux", "OpenSUSE", "Solus", "MX Linux"]
    os_choice = random.choice(operating_systems)

    carriers = [
        "Robi", "AT&T", "Verizon", "T-Mobile", "Vodafone", "Orange", "Telekom", "O2", "BT", 
        "Movistar", "Claro", "Telstra", "Sprint", "Airtel", "Reliance Jio", "China Mobile", 
        "China Telecom", "China Unicom", "NTT DoCoMo", "SoftBank", "KDDI", "SK Telecom", 
        "KT Corporation", "LG Uplus", "TIM", "Wind Tre", "Bouygues Telecom", "SFR", "Telkomsel", 
        "Indosat Ooredoo", "XL Axiata", "Smartfren", "TrueMove", "AIS", "DTAC", "MTN", "Vodacom", 
        "Cell C", "Telstra", "Optus", "Singtel", "StarHub", "M1", "Globe Telecom", "Smart Communications", 
        "PLDT", "Digicel", "Claro Brazil", "Oi", "TIM Brasil", "Vivo", "Entel", "Movilnet", "Claro Peru", 
        "Entel Chile", "Tigo", "Personal", "Claro Argentina", "Movistar Argentina", "Movistar Venezuela", 
        "Claro Colombia", "Movistar Colombia", "Movistar Mexico", "Claro Ecuador", "CNT Ecuador", 
        "Movistar Uruguay", "Claro Uruguay", "U Mobile", "Maxis", "Celcom", "Digi Telecommunications", 
        "Free Mobile", "Bouygues Telecom", "SFR", "Wind Hellas", "Cosmote", "MTN Cyprus", 
        "Vodafone Cyprus", "Telecom Italia", "KPN", "Telfort", "Vodafone Netherlands", "Proximus", 
        "Orange Belgium", "BASE", "Swisscom", "Sunrise", "Salt Mobile", "A1 Telekom Austria", 
        "T-Mobile Austria", "Magenta Telekom", "Hutchison Drei Austria", "Telenor", "Telia", "Elisa", 
        "DNA", "Tele2", "Megafon", "MTS", "Beeline", "Tele2 Russia", "Kyivstar", "Vodafone Ukraine", 
        "Lifecell", "Moldcell", "Orange Moldova", "Unitel Mongolia", "G-Mobile", "Mobicom", "Ooredoo Myanmar", 
        "MPT", "Telenor Myanmar", "STC", "Mobily", "Zain", "Du", "Etisalat", "Batelco", "Viva Bahrain", 
        "Ooredoo Qatar", "Vodafone Qatar", "Omantel", "Ooredoo Oman", "Tata DoCoMo", "BSNL", "MTNL"
    ]
    carrier = random.choice(carriers)

    user_agent = (
        f"[FBAN/FBWEB;FBAV/{fbav};FBBV/{fbbv};"
        f"FBDM{{density={density},width={width},height={height}}};"
        f"FBLC/{fblc};FBRV/{fbrv};"
        f"FBCR/{carrier};FBMF/{manufacturer};FBBD/{manufacturer};"
        f"FBPN/{fbpn};FBDV/{model};FBSV/{fbsrv};FBOP/{fbop};FBCA/{fbca};]"
    )
    return user_agent

def lines():
    print("="*os.get_terminal_size().columns)
pr=p1.ask
def main():
    lines()
    #print("="*os.get_terminal_size().columns)
    rp("[bold yellow][[bold cyan]1[bold yellow]] COOKIE GETTER\n[bold yellow][[bold cyan]2[bold yellow]] BOT DETECTION\n[bold yellow][[bold cyan]3[bold yellow]] BOT DETECTION FIXER")
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
                headers={
                        'User-Agent': ua(),                #"[FBAN/FB4A;FBAV/196.0.0.29.99;FBPN/com.facebook.katana;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]','[FBAN/Orca-Android;FBAV/249.0.0.10.122;FBBV/415015957;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/TNT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-A546S;FBSV/8.0;FBCA/armeabi-v7a:armeabi;]",
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
        pass
def bd():
    sm('clear')
    fi=pr("[bold yellow]Enter Your FileList(uid•pass•cookie)")
    xx=open(fi,"r").read().splitlines()
    with ter(max_workers=5) as botd:
        for o in xx:
            uid, passw, cook=o.split("•")
            botd.submit(botdetected,uid,passw,cook)
botdd=0
def botdetected(uid,passw,cook):
    global loop, botdd
    try:
        sys.stdout.write("\r\033[1;37mBOTDETECT(%s) BOTD:-%s"%(loop,botdd))
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
        else:
            print("\r\033[1;32m[NO BOT DETECTED] %s|%s"%(uid,passw))
        loop+=1
    except Exception as e:
        pass
def cookiegg():
    sm('clear')
    fi=p1.ask("[bold yellow]Enter Account List")
    xx=open(fi,"r").read().splitlines()
    with ter(max_workers=10) as cg:
        for i in xx:
            uid,passw=i.split("|")
            cg.submit(cookieg,uid,passw)
def cookieg(uid,passw):
    global loop,ok,cp
    try:
        sys.stdout.write("\r\033[1;37mCOOKIE(%s)OK:-%s CP:-%s"%(loop,ok,cp))
        headers={
          'User-Agent': ua(),       #"[FBAN/FB4A;FBAV/196.0.0.29.99;FBPN/com.facebook.katana;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]','[FBAN/FB4A;FBAV/196.0.0.29.99;FBPN/com.facebook.katana;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
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
        #print(pos)
        if "session_key" in pos:
            cookies=f"sb={''.join(random.choices(string.ascii_letters+string.digits+'_',k=24))};"+';'.join(i['name']+'='+i['value'] for i in pos['session_cookies'])
            xx=requests.get('https://graph.facebook.com/'+uid+'/picture?type=normal').text
            if "Photoshop" in xx:
                ok+=1
                print("\r\033[1;32m[SUCCESS] %s|%s|%s"%(uid,passw,cookies))
                print("SAVE IN: \033[1;36m/sdcard/success-cookies.txt")
                if uid in open("/sdcard/success-cookies.txt","r").read():
                    pass
                else:
                    open("/sdcard/success-cookies.txt","a").write("%s•%s•%s\n"%(uid,passw,cookies))
                    open("/sdcard/at.txt","a").write("%s\n"%(pos['access_token']))
            else:
                cp+=1
                print("\r\033[1;31m[FAILED] %s|%s"%(uid,passw))
        elif "www.facebook.com" in pos['error']['message']:
            cp+=1
            print("\r\033[1;31m[FAILED] %s|%s"%(uid,passw))
        elif "Invalid username or password" in str(pos):
            print("\r\033[1;36m[INVALID] %s|%s"%(uid,passw))
        elif "You Entered an Older Password" in pos['error']['error_user_title']:
          print("\r\033[1;33m[CHANGED PASS] %s|%s"%(uid,passw))
        loop+=1
    except Exception as e:
        pass
main()
