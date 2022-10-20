from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import fonksiyonlar


browser = webdriver.Chrome("C:/Users/ay_oz/Desktop/KargoPython/chromedriver.exe")
browser.get("https://www.ups.com.tr/gonderi_takip.aspx")

takipNo = browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_text_yurtici2_takip"]')
login = browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_buton2_yurtici_takip"]')

takipNumarasi = "1Z1E88V36843244142"
takipNo.send_keys(takipNumarasi)
login.click()
time.sleep(1)
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
next = browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_LinkButtonSonIslemGoster"]')
next.click()
time.sleep(3)
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
hareketler = browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_DataListSonIslem"]/tbody')
hareketSayisi = fonksiyonlar.hareketsayisigetir(hareketler) - 1 
print("Hareket Sayısı : ",hareketSayisi)
list =[]
for i in range(hareketSayisi):
    islemTarihi = browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_DataListSonIslem_ctl0{}_Label5"]'.format(i+1))
    islem = browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_DataListSonIslem_ctl0{}_Label24"]'.format(i+1))
    hareketYeri = browser.find_element(By.XPATH,'//*[@id="ctl00_MainContent_DataListSonIslem_ctl0{}_Label25"]'.format(i+1))
    a = fonksiyonlar.hareketler(islemTarihi,hareketYeri,islem)
    list.append(a)
list.reverse()
print(list)

