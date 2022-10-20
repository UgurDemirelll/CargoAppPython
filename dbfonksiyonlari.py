import pyrebase
import dbfonksiyonlari
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import mysql.connector
from mysql.connector import (connection)
mydb = mysql.connector.connect(user='root', 
                            password='1010114214',
                              host='127.0.0.1',
                              auth_plugin = 'mysql_native_password',
                              database = 'kargo'
                              )

firebaseConfig = {'apiKey': "AIzaSyClIWeT-uwCWfy1c9WXxjjRr60pcDoVXQ0",
  'authDomain': "cargo-964c3.firebaseapp.com",
  'databaseURL': "https://cargo-964c3-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "cargo-964c3",
  'storageBucket': "cargo-964c3.appspot.com",
  'messagingSenderId': "37575557630",
  'appId': "1:37575557630:web:05be24e89637057284c0af"}

def yeniKargo(firebaseIdList,mysqlIdList):
    yeniKargoList =[]
    kaydedilmisList = []
    print(len(firebaseIdList))
    print(len(mysqlIdList))
    for i in range(len(firebaseIdList)):
        if firebaseIdList[i][0] == mysqlIdList[i][0]:
            print("kayıtlı")
            kaydedilmisList.append(firebaseIdList[i])
        else:
            print("kaydedilecek")
            yeniKargoList.append(firebaseIdList[i])
    return yeniKargoList

def guncelKargo(firebaseIdList,mysqlIdList):
    guncelList=[]
    for i in firebaseIdList:
        if mysqlIdList.count(i) == 0:
            guncelList.append(i)  
    return guncelList

# def firebasedenIdListesiAl():
#     cred = credentials.Certificate('firebase-sdk.json')
#     firebase_admin.initialize_app(cred,{
#     'databaseURL' : 'https://cargo-964c3-default-rtdb.europe-west1.firebasedatabase.app/'
#     })
#     kargoList = ["hepsijet","mngKargo","pttKargo","suratKargo"]
#     firebaseIdList = []
#     for kargo in kargoList:
#         ref = db.reference(kargo)
#         firebaseTumKargolar = ref.get() 
#         for i in firebaseTumKargolar:
#             id = i
#             aralist = [id,kargo]
#             firebaseIdList.append(aralist)
#             print("id: ",id)
#     return firebaseIdList

def firebasedenIdListesiAl():
    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    kargoList = ["hepsijet","mngKargo","pttKargo","suratKargo","upsKargo","arasKargo"]
    firebaseIdList = []
    for kargo in kargoList:
        liste = dict(db.child(kargo).get().val())
        for i in liste:
            if liste[i]['hareketYeri'] == '':
                id = i
                aralist = [id,kargo]
                firebaseIdList.append(aralist)
                print("id: ",id)           
    return firebaseIdList

def tumFirebaseIdList():
    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    kargoList = ["hepsijet","mngKargo","pttKargo","suratKargo","upsKargo","arasKargo"]
    firebaseIdList = []
    for kargo in kargoList:
        liste = dict(db.child(kargo).get().val())
        for i in liste:
            id = i
            aralist = [id,kargo]
            firebaseIdList.append(aralist)
    return firebaseIdList        



def mysqldenIdListesiAl():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT id FROM hepsijet WHERE hareketNo = 0')
    hepsijetList = mycursor.fetchall()
    mysqlIdListesi = []
    for hepsi in hepsijetList:
        aralist = [hepsi[0],"hepsijet"]
        mysqlIdListesi.append(aralist)
    mycursor.execute('SELECT id FROM mngKargo WHERE hareketNo = 0')
    mngKargoList = mycursor.fetchall()
    for hepsi in mngKargoList:
        aralist = [hepsi[0],"mngKargo"]
        mysqlIdListesi.append(aralist)
    mycursor.execute('SELECT id FROM pttKargo WHERE hareketNo = 0')
    pttKargoList = mycursor.fetchall()
    for hepsi in pttKargoList:
        aralist = [hepsi[0],"pttKargo"]
        mysqlIdListesi.append(aralist)
    mycursor.execute('SELECT id FROM suratKargo WHERE hareketNo = 0')
    suratKargoList = mycursor.fetchall()
    for hepsi in suratKargoList:
        aralist = [hepsi[0],'suratKargo']
        mysqlIdListesi.append(aralist)
    mycursor.execute('SELECT id FROM upsKargo WHERE hareketNo = 0')
    upsKargoList = mycursor.fetchall()
    for hepsi in upsKargoList:
        aralist = [hepsi[0],'upsKargo']
        mysqlIdListesi.append(aralist)
    mycursor.execute('SELECT id FROM arasKargo WHERE hareketNo = 0')
    arasKargoList = mycursor.fetchall()
    for hepsi in arasKargoList:
        aralist = [hepsi[0],'arasKargo']
        mysqlIdListesi.append(aralist)
    return mysqlIdListesi

def tumMydbIdList():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT id FROM hepsijet')
    hepsijetList = mycursor.fetchall()
    mysqlIdListesi = []
    for hepsi in hepsijetList:
        aralist = [hepsi[0],"hepsijet"]
        mysqlIdListesi.append(aralist)
    mycursor.execute('SELECT id FROM mngKargo')
    mngKargoList = mycursor.fetchall()
    for hepsi in mngKargoList:
        aralist = [hepsi[0],"mngKargo"]
        mysqlIdListesi.append(aralist)
    mycursor.execute('SELECT id FROM pttKargo')
    pttKargoList = mycursor.fetchall()
    for hepsi in pttKargoList:
        aralist = [hepsi[0],"pttKargo"]
        mysqlIdListesi.append(aralist)
    mycursor.execute('SELECT id FROM suratKargo')
    suratKargoList = mycursor.fetchall()
    for hepsi in suratKargoList:
        aralist = [hepsi[0],'suratKargo']
        mysqlIdListesi.append(aralist)
    mycursor.execute('SELECT id FROM upsKargo')
    upsKargoList = mycursor.fetchall()
    for hepsi in upsKargoList:
        aralist = [hepsi[0],'upsKargo']
        mysqlIdListesi.append(aralist)
    mycursor.execute('SELECT id FROM arasKargo')
    arasKargoList = mycursor.fetchall()
    for hepsi in arasKargoList:
        aralist = [hepsi[0],'arasKargo']
        mysqlIdListesi.append(aralist)
    return mysqlIdListesi

def mysqleKaydet(kaydedilecekIdList):       
    for i in kaydedilecekIdList:
        firebase = pyrebase.initialize_app(firebaseConfig)
        dbf = firebase.database()
        mycursor = mydb.cursor()
        data = dbf.child(i[1]).child(i[0]).get().val()
        print(data)
        sql = "INSERT INTO {} (id,hareketNo,hareketYeri,islem,islemTarihi,takipNo,urunNo,user) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)".format(i[1])
        print("islem : ",data['islem'])
        values =  (i[0],data['hareketNo'],data['hareketYeri'],data['islem'],data['islemTarihi'],data['takipNo'],data['urunNo'],str(data['user']))
        mycursor.execute(sql,values)
        mydb.commit()
def mysqldenHareketSayisiAl(kargo,takipNo):
    mycursor = mydb.cursor()
    mycursor.execute('SELECT id FROM {} WHERE takipNo = {}'.format(kargo,takipNo))
    list = mycursor.fetchall()

def mysqldenTakipNoListesiAl():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT takipNo FROM hepsijet where hareketNo = 0')
    hepsijetList = mycursor.fetchall()
    mysqlTakipNoListesi = []
    for hepsi in hepsijetList:
        aralist = [hepsi[0],"hepsijet"]
        mysqlTakipNoListesi.append(aralist)
    mycursor.execute('SELECT takipNo FROM mngKargo where hareketNo = 0')
    mngKargoList = mycursor.fetchall()
    for hepsi in mngKargoList:
        aralist = [hepsi[0],"mngKargo"]
        mysqlTakipNoListesi.append(aralist)
    mycursor.execute('SELECT takipNo FROM pttKargo where hareketNo = 0')
    pttKargoList = mycursor.fetchall()
    for hepsi in pttKargoList:
        aralist = [hepsi[0],"pttKargo"]
        mysqlTakipNoListesi.append(aralist)
    mycursor.execute('SELECT takipNo FROM suratKargo where hareketNo = 0')
    suratKargoList = mycursor.fetchall()
    for hepsi in suratKargoList:
        aralist = [hepsi[0],"suratKargo"]
        mysqlTakipNoListesi.append(aralist)
    mycursor.execute('SELECT takipNo FROM upsKargo where hareketNo = 0')
    upsList = mycursor.fetchall()
    for hepsi in upsList:
        aralist = [hepsi[0],"upsKargo"]
        mysqlTakipNoListesi.append(aralist)
    mycursor.execute('SELECT takipNo FROM arasKargo where hareketNo = 0')
    arasList = mycursor.fetchall()
    for hepsi in arasList:
        aralist = [hepsi[0],"arasKargo"]
        mysqlTakipNoListesi.append(aralist)
    return mysqlTakipNoListesi

def mysqlKargoHareket(takipNumarasi,kargo):
    mydb = mysql.connector.connect(user='root', password='1010114214',host='127.0.0.1', auth_plugin = 'mysql_native_password',database = 'kargo')
    mycursor = mydb.cursor()
    mycursor.execute(f'SELECT * FROM {kargo} WHERE takipNo = {takipNumarasi}')
    listmysql = mycursor.fetchall()
    return listmysql, len(listmysql)

def userAl(kargo,takipNumarasi):
    mydb = mysql.connector.connect(user='root', password='1010114214',host='127.0.0.1', auth_plugin = 'mysql_native_password',database = 'kargo')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT user FROM {} WHERE takipNo = {}'.format(kargo,takipNumarasi))
    user = mycursor.fetchone()
    return user

def mysqlPttKargoHareket(takipNumarasi,kargo):
    mycursor = mydb.cursor()
    mycursor.execute(f'SELECT takipNo FROM {kargo}')
    takipNoList = mycursor.fetchall()
    hareketSayisi = 0
    for t in range(len(takipNoList)):
        hareketSayisi += takipNoList[t].count(takipNumarasi)
    mycursor.execute(f'SELECT * FROM {kargo}')
    listmysql = mycursor.fetchall()
    list = []
    for i in listmysql:
        if i[5] == takipNumarasi:
            list.append(i)
    return list, hareketSayisi

def userAlPtt(kargo,takipNumarasi):
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM {}'.format(kargo))
    userlist = mycursor.fetchall()
    user = ""
    for i in userlist:
        if i[5] == takipNumarasi:
            user = i[7]
            break
    return user
