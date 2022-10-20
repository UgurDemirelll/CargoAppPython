import mysql.connector
from mysql.connector import (connection)

import pyrebase

firebaseConfig = {'apiKey': "AIzaSyClIWeT-uwCWfy1c9WXxjjRr60pcDoVXQ0",
  'authDomain': "cargo-964c3.firebaseapp.com",
  'databaseURL': "https://cargo-964c3-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "cargo-964c3",
  'storageBucket': "cargo-964c3.appspot.com",
  'messagingSenderId': "37575557630",
  'appId': "1:37575557630:web:05be24e89637057284c0af"}


mydb = mysql.connector.connect(user='root', 
                            password='1010114214',
                              host='127.0.0.1',
                              auth_plugin = 'mysql_native_password',
                              database = 'kargo'
                              )


mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM {} WHERE takipNo = {}'.format('hepsijet',"62750418825684"))
listmysql = mycursor.fetchall()
print(len(listmysql))
print(listmysql)
print(type(listmysql))
mysqlDict = {}
for i in listmysql:
  mysqlDict.update({i[0]:{
    "hareketNo":int(i[1]),
    "hareketYeri":i[2],
    "islem":i[3],
    "islemTarihi":i[4],
    "takipNo":i[5],
    "urunNo":int(i[6]),
    "user":i[7]
  }})
print("mysql dict : ",mysqlDict)
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
firebaseDict = db.child("hepsijet").order_by_child("takipNo").equal_to("").get()
print("firebase dict : ",dict(firebaseDict.val()))
print(type(firebaseDict.val()))

print(mysqlDict==dict(firebaseDict.val()))
