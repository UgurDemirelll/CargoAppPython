
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import fonksiyonlar

def hepsijetHareket(takipNumarasi):
    browser = webdriver.Chrome("C:/Users/ay_oz/Desktop/KargoPython/chromedriver.exe")
    browser.get("https://kargomnerede.co/kargolar/hepsijet")
    takipNo = browser.find_element(By.XPATH,'//*[@id="__next"]/section/div/div/div[1]/div[1]/div/form/div[1]/textarea')
    login = browser.find_element(By.XPATH,'//*[@id="__next"]/section/div/div/div[1]/div[1]/div/form/div[3]/div/button/span')
    takipNo.send_keys(takipNumarasi)
    login.click()
    time.sleep(1)
    hareketler = browser.find_element(By.XPATH,'//*[@id="__next"]/section/div/div[2]/div/div[2]/div[1]/div[2]')
    hareketSayisi = int(fonksiyonlar.hareketsayisigetir(hareketler)/2)
    print("Hareket Sayısı : ",hareketSayisi)
    list = []
    list = fonksiyonlar.hareketListGetir(hareketler)
    list.reverse()
    sonList = []
    for i in list:
        sonList.append(i.split("-"))
    ensonList = []
    for i in range(hareketSayisi):
        ensonList.append((sonList[2*i][0],sonList[2*i][1],sonList[(2*i)+1][0]))
    return hareketSayisi,ensonList

def mngKargoHareket(takipNumarasi):
    browser = webdriver.Chrome('C:/Users/ay_oz/Desktop/KargoPython/chromedriver.exe')
    browser.get("https://www.mngkargo.com.tr/gonderitakip")
    
    sifre = browser.find_element(By.XPATH, '//*[@id="captcha1"]/div/span').text
    sifre = sifre.replace(" ","")
    sifreText = browser.find_element(By.XPATH,'//*[@id="captcha1"]/input')
    login = browser.find_element(By.XPATH, '//*[@id="shipmentFormStandard"]/div[2]/a')
    takipNo = browser.find_element(By.XPATH,'//*[@id="form_shipment"]')
    takipNo.send_keys(takipNumarasi)
    sifreText.send_keys(sifre)
    login.click()
    time.sleep(1)
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    login1 = browser.find_element(By.XPATH, '/html/body/main/section/div/div[2]/div/div/div[1]/div[2]/div[2]/div[1]')
    login1.click()
    hareketler = browser.find_element(By.XPATH, '/html/body/main/section/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/ul')
    hareketSayisi = hareketler.text.count("Transfer Aşamasında")+hareketler.text.count("Teslim Edildi")+hareketler.text.count("Alıcı Adresine Yönlendirildi")+hareketler.text.count("Varış Birimine Ulaştı")+hareketler.text.count("Gönderi Hazırlandı")
    list = []
    for hareket in range(hareketSayisi):        
        islemTarihi = browser.find_element(By.XPATH,'/html/body/main/section/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/ul/li[{}]/div[3]/div[2]'.format(hareket+1))
        hareketYeri = browser.find_element(By.XPATH,'/html/body/main/section/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/ul/li[{}]/div[3]/div[3]'.format(hareket+1))
        islem = browser.find_element(By.XPATH,'/html/body/main/section/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/ul/li[{}]/div[3]/div[1]/div[1]'.format(hareket+1))
        a = fonksiyonlar.hareketler(islemTarihi,hareketYeri,islem)
        list.append(a)
    list.reverse()
    return hareketSayisi,list

def pttKargoHareket(takipNumarasi):
    kargoAdi = "pttKargo"
    browser = webdriver.Chrome("C:/Users/ay_oz/Desktop/KargoPython/chromedriver")
    browser.get("https://gonderitakip.ptt.gov.tr/")
    login = browser.find_element(By.XPATH, '//*[@id="searchButton"]/i')
    takipNo = browser.find_element(By.XPATH,'//*[@id="search-area"]')
    takipNo.send_keys(takipNumarasi) # fonksiyonu tanımladığımızda bu veriyi alacak
    login.click()
    login = browser.find_element(By.XPATH, '//*[@id="activityButton"]/img')
    login.click()
    time.sleep(1)
    hareketler = browser.find_element(By.XPATH, '//*[@id="shipActivity"]/div/div/table/tbody')
    hareketSayisi = fonksiyonlar.hareketsayisigetir(hareketler)
    list = []
    for hareket in range(hareketSayisi):        
        islemTarihi = browser.find_element(By.XPATH,'//*[@id="shipActivity"]/div/div/table/tbody/tr[{}]/td[1]'.format(hareket+1))
        hareketYeri = browser.find_element(By.XPATH,'//*[@id="shipActivity"]/div/div/table/tbody/tr[{}]/td[4]'.format(hareket+1))
        islem = browser.find_element(By.XPATH,'//*[@id="shipActivity"]/div/div/table/tbody/tr[{}]/td[2]'.format(hareket+1))
        a = fonksiyonlar.hareketler(islemTarihi,hareketYeri,islem)
        list.append(a)
    return hareketSayisi,list

def suratKargoHareket(takipNumarasi,urunsayisi):
    browser = webdriver.Chrome("C:/Users/ay_oz/Desktop/KargoPython/chromedriver.exe")
    browser.get("http://suratkargo.com.tr/KargoTakip/")
    login = browser.find_element(By.XPATH, "/html/body/div[2]/section/form/div[1]/div[3]/div/button")
    takipNo = browser.find_element(By.XPATH,"/html/body/div[2]/section/form/div[1]/div[2]/input")
    takipNo.send_keys(takipNumarasi) 
    login.click()
    hareketSayisi = 0
    toplamHareketSayisi = 0
    list = []
    list.clear
    urun = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[5]/table/tbody/tr[{}]/td[8]/button".format(urunsayisi+1))
    urun.click()
    time.sleep(1)
    browser.back
    time.sleep(1)
    hareketler = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[7]/table/tbody")
    hareketSayisi = fonksiyonlar.hareketsayisigetir(hareketler)
    toplamHareketSayisi = toplamHareketSayisi + hareketSayisi   
    for hareket in range(hareketSayisi):        
        islemTarihi = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[7]/table/tbody/tr[{}]/td[1]/span".format(hareket+1))
        hareketYeri = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[7]/table/tbody/tr[{}]/td[2]/span".format(hareket+1))
        islem = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[7]/table/tbody/tr[{}]/td[3]/span".format(hareket+1))
        a = fonksiyonlar.hareketler(islemTarihi,hareketYeri,islem)
        list.append(a)
    list.reverse()
    return toplamHareketSayisi,list

def suratKargoUrunSayisi(takipNumarasi):
    browser = webdriver.Chrome("C:/Users/ay_oz/Desktop/KargoPython/chromedriver.exe")
    browser.get("http://suratkargo.com.tr/KargoTakip/")
    login = browser.find_element(By.XPATH, "/html/body/div[2]/section/form/div[1]/div[3]/div/button")
    takipNo = browser.find_element(By.XPATH,"/html/body/div[2]/section/form/div[1]/div[2]/input")
    takipNo.send_keys(takipNumarasi) # fonksiyonu tanımladığımızda bu veriyi alacak
    login.click()
    kargoAdi = "suratKargo"
    urunler = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[5]/table/tbody")
    urunsayisi = []
    for i in urunler.text:
        urunsayisi.append(i)
    urunsayisi = "".join(urunsayisi)
    urunsayisi = urunsayisi.split("\n")
    urunsayisi = len(urunsayisi)
    print("Ürün Sayısı : ",urunsayisi)
    return urunsayisi

def upsKargoHareket(takipNumarasi):
    browser = webdriver.Chrome("C:/Users/ay_oz/Desktop/KargoPython/chromedriver.exe")
    browser.get("https://www.ups.com.tr/gonderi_takip.aspx")
    takipNo = browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_text_yurtici2_takip"]')
    login = browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_buton2_yurtici_takip"]')
    takipNo.send_keys(takipNumarasi)
    login.click()
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    next = browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_LinkButtonSonIslemGoster"]')
    next.click()
    time.sleep(1)
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    hareketler = browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_DataListSonIslem"]/tbody')
    hareketSayisi = fonksiyonlar.hareketsayisigetir(hareketler) - 1 
    list = []
    for i in range(hareketSayisi):
        islemTarihi = browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_DataListSonIslem_ctl0{}_Label5"]'.format(i+1))
        islem = browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_DataListSonIslem_ctl0{}_Label24"]'.format(i+1))
        hareketYeri = browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_DataListSonIslem_ctl0{}_Label25"]'.format(i+1))
        a = fonksiyonlar.hareketler(islemTarihi,hareketYeri,islem)
        list.append(a)
    list.reverse()
    return hareketSayisi,list

def arasKargoHareket(takipNumarasi):
    browser = webdriver.Chrome("C:/Users/ay_oz/Desktop/KargoPython/chromedriver.exe")
    browser.get("https://kargomnerede.co/kargolar/aras-kargo")
    takipNo = browser.find_element(By.XPATH,'//*[@id="__next"]/section/div/div/div[1]/div[1]/div/form/div[1]/textarea')
    login = browser.find_element(By.XPATH,'//*[@id="__next"]/section/div/div/div[1]/div[1]/div/form/div[3]/div/button/span')
    takipNo.send_keys(takipNumarasi)
    login.click()
    time.sleep(1)
    hareketler = browser.find_element(By.XPATH,'//*[@id="__next"]/section/div/div[2]/div/div[2]/div[1]/div[2]')
    hareketSayisi = int(fonksiyonlar.hareketsayisigetir(hareketler)/2)
    list = []
    list = fonksiyonlar.hareketListGetir(hareketler)
    list.reverse()
    sonList = []
    for i in range (hareketSayisi):
        islemTarihi = list[i*2].split("-")[0]
        print(islemTarihi)
        islemYeri = list[i*2].split("-")[1]
        print(islemYeri)
        islem = list[(2*i)+1]
        print(islem)
        sonList.append((islemTarihi,islemYeri,islem))
    return hareketSayisi,sonList



