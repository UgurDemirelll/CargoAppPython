
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import fonksiyonlar



browser = webdriver.Chrome("C:/Users/ay_oz/Desktop/KargoPython/chromedriver.exe")
browser.get("http://suratkargo.com.tr/KargoTakip/")
time.sleep(1)
login = browser.find_element(By.XPATH, "/html/body/div[2]/section/form/div[1]/div[3]/div/button")
takipNo = browser.find_element(By.XPATH,"/html/body/div[2]/section/form/div[1]/div[2]/input")
takipNumarasi = "24822413812816"
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
hareketSayisi = 0
list = []
for i in range(urunsayisi):
    list.clear
    print(i)
    urun = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[5]/table/tbody/tr[{}]/td[8]/button".format(i+1))
    urun.click()
    time.sleep(1)
    browser.back
    time.sleep(1)
    hareketler = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[7]/table/tbody")
    hareketSayisi = fonksiyonlar.hareketsayisigetir(hareketler)
    for hareket in range(hareketSayisi):        
        islemTarihi = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[7]/table/tbody/tr[{}]/td[1]/span".format(hareket+1))
        hareketYeri = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[7]/table/tbody/tr[{}]/td[2]/span".format(hareket+1))
        islem = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[7]/table/tbody/tr[{}]/td[3]/span".format(hareket+1))
        a = fonksiyonlar.hareketler(islemTarihi,hareketYeri,islem)
        list.append(a)
list.reverse()
print(list)


