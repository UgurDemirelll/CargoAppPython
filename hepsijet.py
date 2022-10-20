
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import fonksiyonlar

def hepsijet(takipNumarasi,urunNo,user):
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
    onlineDict = {}
    list = fonksiyonlar.hareketListGetir(hareketler)
    list.reverse()
    print(list)
    for i in range (hareketSayisi):
        islemTarihi = list[i*2].split("-")[0]
        print(islemTarihi)
        hareketYeri = list[i*2].split("-")[1]
        print(hareketYeri)
        islem = list[(2*i)+1]
        print(islem)
        onlineDict.update({"hareketNo":i+1,  
        "hareketYeri":hareketYeri,
        "islem":islem,
        "islemTarihi":islemTarihi,
        "takipNo":takipNumarasi,
        "urunNo":urunNo,
        "user":user
        })
    return onlineDict