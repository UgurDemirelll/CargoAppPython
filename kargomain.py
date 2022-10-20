# 1 = firebaseden kargo bilgilerini alacağız ++
# 1.5 = mysql ile firebase farklımı kontrol edeceğiz ++
# 1.75 = farklı olanları kaydedeceğiz ++
# 2 = mysql e kaydedeceğiz ++
# 3 = aldığımız verilere göre internetten veri çekeceğiz
# 4 = çektiğimiz veriler ile mysql farklı ise firebase yi güncelleyeceğiz
# 5 = firebase de değişiklik olduğunda ilgili kullanıcıya 
# 

import pyrebase
import dbfonksiyonlari
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import mysql.connector
from mysql.connector import (connection)
import kargolar


firebaseConfig = {'apiKey': "AIzaSyClIWeT-uwCWfy1c9WXxjjRr60pcDoVXQ0",
  'authDomain': "cargo-964c3.firebaseapp.com",
  'databaseURL': "https://cargo-964c3-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "cargo-964c3",
  'storageBucket': "cargo-964c3.appspot.com",
  'messagingSenderId': "37575557630",
  'appId': "1:37575557630:web:05be24e89637057284c0af"}

firebase = pyrebase.initialize_app(firebaseConfig)
dbf = firebase.database()

firebaseIdList = dbfonksiyonlari.firebasedenIdListesiAl()
print("firebase id listesi : ",firebaseIdList)

mydb = mysql.connector.connect(user='root', 
                            password='1010114214',
                              host='127.0.0.1',
                              auth_plugin = 'mysql_native_password',
                              database = 'kargo'
                              )


mysqlIdListesi = dbfonksiyonlari.mysqldenIdListesiAl()
tumfirebaseIdList = dbfonksiyonlari.tumFirebaseIdList()
tumMydbIdList = dbfonksiyonlari.tumMydbIdList()  
print("mysql id list: ",mysqlIdListesi)
kaydedilecekIdList = []
silinecekList = []
if len(tumMydbIdList) == 0:
  kaydedilecekIdList = tumfirebaseIdList
elif tumfirebaseIdList == tumMydbIdList:
    kaydedilecekIdList = []
elif len(tumfirebaseIdList) > len(tumMydbIdList):
    kaydedilecekIdList = dbfonksiyonlari.guncelKargo(tumfirebaseIdList,tumMydbIdList)
elif len(tumfirebaseIdList) < len(tumMydbIdList):
    silinecekList = dbfonksiyonlari.guncelKargo(tumfirebaseIdList,tumMydbIdList)
print("kaydedilecek liste : ",kaydedilecekIdList)
if len(kaydedilecekIdList) != 0:
  dbfonksiyonlari.mysqleKaydet(kaydedilecekIdList)

# mysql den takipnumaralarını alıyoruz
takipNoList = dbfonksiyonlari.mysqldenTakipNoListesiAl()
print(takipNoList)

# mysqldeki hareket sayısını alacağız
kargoListesi = ["hepsijet","mngKargo","pttKargo","suratKargo","upsKargo","arasKargo"]
intHareketSayisi = 0
mysqlHareketSayisi = 0
mysqlList = []
intList = []
intUrunSayisi = 0
for takip in takipNoList:
  if takip[1] == "hepsijet":
    intHareketSayisi, intList = kargolar.hepsijetHareket(takip[0])
    mysqlList,mysqlHareketSayisi = dbfonksiyonlari.mysqlKargoHareket(takip[0],"hepsijet")
    user = dbfonksiyonlari.userAl("hepsijet",takip[0])
    print("hepsijet user : ",user)
    if intHareketSayisi + 1 != mysqlHareketSayisi:
        for i in range(intHareketSayisi-mysqlHareketSayisi+1):
          data = {"hareketNo":str(i+mysqlHareketSayisi),
          "hareketYeri":intList[i+mysqlHareketSayisi-1][1],
          "islem":intList[i+mysqlHareketSayisi-1][2],
          "islemTarihi":intList[i+mysqlHareketSayisi-1][0],
          "takipNo":str(takip[0]),
          "urunNo":"1",
          "user":str(user)}
          dbf.child("hepsijet").push(data)

  if takip[1] == "mngKargo":
    intHareketSayisi, intList = kargolar.mngKargoHareket(takip[0])
    print("1",intHareketSayisi)
    print("2",intList)
    print("3",takip[0])
    mysqlList,mysqlHareketSayisi = dbfonksiyonlari.mysqlKargoHareket(takip[0],"mngKargo")
    user = dbfonksiyonlari.userAl("mngKargo",takip[0])
    if intHareketSayisi + 1 != mysqlHareketSayisi:
        for i in range(intHareketSayisi-mysqlHareketSayisi+1):
          data = {"hareketNo":str(i+mysqlHareketSayisi),
          "hareketYeri":intList[i+mysqlHareketSayisi-1][1],
          "islem":intList[i+mysqlHareketSayisi-1][2],
          "islemTarihi":intList[i+mysqlHareketSayisi-1][0],
          "takipNo":str(takip[0]),
          "urunNo":"1",
          "user":user}
          dbf.child("mngKargo").push(data)
  if takip[1] == "pttKargo":
    intHareketSayisi,intList = kargolar.pttKargoHareket(takip[0])
    mysqlList,mysqlHareketSayisi = dbfonksiyonlari.mysqlPttKargoHareket(takip[0],"pttkargo")
    user = dbfonksiyonlari.userAlPtt("pttKargo",takip[0])
    if intHareketSayisi + 1 != mysqlHareketSayisi:
        for i in range(intHareketSayisi-mysqlHareketSayisi+1):
          data = {"hareketNo":str(i+mysqlHareketSayisi),
          "hareketYeri":intList[i+mysqlHareketSayisi-1][1],
          "islem":intList[i+mysqlHareketSayisi-1][2],
          "islemTarihi":intList[i+mysqlHareketSayisi-1][0],
          "takipNo":str(takip[0]),
          "urunNo":"1",
          "user":user}
          dbf.child("pttKargo").push(data)
  if takip[1] == "suratKargo":
    urunsayisi = kargolar.suratKargoUrunSayisi(takip[0])
    for u in range(urunsayisi):
      intHareketSayisi,intList = kargolar.suratKargoHareket(takip[0],u)
      mysqlList,mysqlHareketSayisi = dbfonksiyonlari.mysqlKargoHareket(takip[0],"suratKargo")
      user = dbfonksiyonlari.userAl("suratKargo",takip[0])
      user = user[0]
      if intHareketSayisi + 1 != mysqlHareketSayisi:
          for i in range(intHareketSayisi-mysqlHareketSayisi+1):
            data = {"hareketNo":str(i+mysqlHareketSayisi),
            "hareketYeri":intList[i+mysqlHareketSayisi-1][1],
            "islem":intList[i+mysqlHareketSayisi-1][2],
            "islemTarihi":intList[i+mysqlHareketSayisi-1][0],
            "takipNo":str(takip[0]),
            "urunNo":str(u+1),
            "user":user}
            dbf.child("suratKargo").push(data)
  if takip[1] == "upsKargo":
    intHareketSayisi,intList = kargolar.upsKargoHareket(takip[0])
    mysqlList,mysqlHareketSayisi = dbfonksiyonlari.mysqlPttKargoHareket(takip[0],"upsKargo")
    user = dbfonksiyonlari.userAlPtt("upsKargo",takip[0])

    print("upsKargo user : ",user)
    if intHareketSayisi + 1 != mysqlHareketSayisi:
        for i in range(intHareketSayisi-mysqlHareketSayisi+1):
          data = {"hareketNo":str(i+mysqlHareketSayisi),
          "hareketYeri":intList[i+mysqlHareketSayisi-1][1],
          "islem":intList[i+mysqlHareketSayisi-1][2],
          "islemTarihi":intList[i+mysqlHareketSayisi-1][0],
          "takipNo":str(takip[0]),
          "urunNo":"1",
          "user":user}
          dbf.child("upsKargo").push(data)
  if takip[1] == "arasKargo":
    intHareketSayisi,intList = kargolar.arasKargoHareket(takip[0])
    mysqlList,mysqlHareketSayisi = dbfonksiyonlari.mysqlKargoHareket(takip[0],"arasKargo")
    user = dbfonksiyonlari.userAl("arasKargo",takip[0])
    print("arasKargo user : ",user)
    if intHareketSayisi + 1 != mysqlHareketSayisi:
        for i in range(intHareketSayisi-mysqlHareketSayisi+1):
          data = {"hareketNo":str(i+mysqlHareketSayisi),
          "hareketYeri":intList[i+mysqlHareketSayisi-1][1],
          "islem":intList[i+mysqlHareketSayisi-1][2],
          "islemTarihi":intList[i+mysqlHareketSayisi-1][0],
          "takipNo":str(takip[0]),
          "urunNo":"1",
          "user":user}
          dbf.child("arasKargo").push(data)

  









