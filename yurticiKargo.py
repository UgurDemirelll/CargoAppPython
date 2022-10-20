from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import fonksiyonlar



browser = webdriver.Chrome("C:/Users/ay_oz/Desktop/KargoPython/chromedriver.exe")
browser.get("https://kargomnerede.co/kargolar/yurtici-kargo")

takipNo = browser.find_element(By.XPATH,'//*[@id="__next"]/section/div/div/div[1]/div[1]/div/form/div[1]/textarea')
login = browser.find_element(By.XPATH,'//*[@id="__next"]/section/div/div/div[1]/div[1]/div/form/div[3]/div/button/span')
takipNumarasi = "62750418825684"
takipNo.send_keys(takipNumarasi)
login.click()
time.sleep(1)
gecersiz=  browser.find_element(By.XPATH,'//*[@id="__next"]/section/div/div[2]/div/div/div[2]/div/div[1]').text
print (gecersiz)

hareketler = browser.find_element(By.XPATH,'//*[@id="__next"]/section/div/div[2]/div/div[2]/div[1]/div[2]')
hareketSayisi = int(fonksiyonlar.hareketsayisigetir(hareketler)/2)
print("Hareket Sayısı : ",hareketSayisi)
list = []

list = fonksiyonlar.hareketListGetir(hareketler)
list.reverse()
for i in range (hareketSayisi):
    islemTarihi = list[i*2].split("-")[0]
    print(islemTarihi)
    islemYeri = list[i*2].split("-")[1]
    print(islemYeri)
    islem = list[(2*i)+1]
    print(islem)