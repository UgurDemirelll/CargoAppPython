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

intHareketSayisi,intList = kargolar.pttKargoHareket("AP05660872431")
mysqlList,mysqlHareketSayisi = dbfonksiyonlari.mysqlPttKargoHareket("AP05660872431","pttkargo")
user = dbfonksiyonlari.userAlPtt("pttKargo","AP05660872431")
print("int sayisi : ",intHareketSayisi)
print("mysql hareket : ",mysqlHareketSayisi)
print(intHareketSayisi + 1 != mysqlHareketSayisi)