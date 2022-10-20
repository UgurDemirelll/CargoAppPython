
from xml.etree.ElementPath import xpath_tokenizer, xpath_tokenizer_re
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import fonksiyonlar
from firebase_admin import credentials
from firebase_admin import db

kargoAdi = "pttKargo"
browser = webdriver.Chrome("C:/Users/ay_oz/Desktop/KargoPython/chromedriver")
browser.get("https://gonderitakip.ptt.gov.tr/")
login = browser.find_element(By.XPATH, '//*[@id="searchButton"]/i')
takipNo = browser.find_element(By.XPATH,'//*[@id="search-area"]')
takipNumarasi = "AP05660872431"
takipNo.send_keys(takipNumarasi) # fonksiyonu tanımladığımızda bu veriyi alacak
login.click()
login = browser.find_element(By.XPATH, '//*[@id="activityButton"]/img')
login.click()
time.sleep(1)
hareketler = browser.find_element(By.XPATH, '//*[@id="shipActivity"]/div/div/table/tbody')

hareketSayisi = fonksiyonlar.hareketsayisigetir(hareketler)
print("Hareket Sayısı : ",hareketSayisi)
list = []
for hareket in range(hareketSayisi):        
    islemTarihi = browser.find_element(By.XPATH,'//*[@id="shipActivity"]/div/div/table/tbody/tr[{}]/td[1]'.format(hareket+1))
    hareketYeri = browser.find_element(By.XPATH,'//*[@id="shipActivity"]/div/div/table/tbody/tr[{}]/td[4]'.format(hareket+1))
    islem = browser.find_element(By.XPATH,'//*[@id="shipActivity"]/div/div/table/tbody/tr[{}]/td[2]'.format(hareket+1))
    a = fonksiyonlar.hareketler(islemTarihi,hareketYeri,islem)
    list.append(a)
#list.reverse()
print(list)
