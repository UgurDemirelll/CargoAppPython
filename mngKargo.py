#from cgitb import reset, text

from selenium import webdriver
import requests
import time
from selenium.webdriver.common.by import By
import fonksiyonlar
#from firebase import firebase
#import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
kargoAdi = "mngKargo"

browser = webdriver.Chrome('C:/Users/ay_oz/Desktop/KargoPython/chromedriver.exe')
browser.get("https://www.mngkargo.com.tr/gonderitakip")
time.sleep(3)
sifre = browser.find_element(By.XPATH, '//*[@id="captcha1"]/div/span').text
sifre = sifre.replace(" ","")
sifreText = browser.find_element(By.XPATH,'//*[@id="captcha1"]/input')
login = browser.find_element(By.XPATH, '//*[@id="shipmentFormStandard"]/div[2]/a')
takipNo = browser.find_element(By.XPATH,'//*[@id="form_shipment"]')
takipNumarasi = "854915753698"
takipNo.send_keys(takipNumarasi)
sifreText.send_keys(sifre)

login.click()

browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
login1 = browser.find_element(By.XPATH, '/html/body/main/section/div/div[2]/div/div/div[1]/div[2]/div[2]/div[1]')
login1.click()

hareketler = browser.find_element(By.XPATH, '/html/body/main/section/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/ul')


hareketSayisi = hareketler.text.count("Transfer Aşamasında")+hareketler.text.count("Teslim Edildi")+hareketler.text.count("Alıcı Adresine Yönlendirildi")+hareketler.text.count("Varış Birimine Ulaştı")+hareketler.text.count("Gönderi Hazırlandı")
print("hareket sayısı : ",hareketSayisi)
list = []
for hareket in range(hareketSayisi):        
    islemTarihi = browser.find_element(By.XPATH,'/html/body/main/section/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/ul/li[{}]/div[3]/div[2]'.format(hareket+1))
    hareketYeri = browser.find_element(By.XPATH,'/html/body/main/section/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/ul/li[{}]/div[3]/div[3]'.format(hareket+1))
    islem = browser.find_element(By.XPATH,'/html/body/main/section/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/ul/li[{}]/div[3]/div[1]/div[1]'.format(hareket+1))
    a = fonksiyonlar.hareketler(islemTarihi,hareketYeri,islem)
    list.append(a)
list.reverse()
print(list[1][2])
print(list)
