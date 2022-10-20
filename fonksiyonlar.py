
import sqlite3
from firebase_admin import db


def hareketsayisigetir(hareketler):  
    hareketlist = []
    for i in hareketler.text:
        hareketlist.append(i)
    hareketlist = "".join(hareketlist)
    hareketlist = hareketlist.split("\n")
    print(hareketlist)
    print("hareket sayısı = ",len(hareketlist))
    return len(hareketlist)

def hareketListGetir(hareketler):
    hareketlist = []
    for i in hareketler.text:
        hareketlist.append(i)
    hareketlist = "".join(hareketlist)
    hareketlist = hareketlist.split("\n")
    print(hareketlist)
    print("hareket sayısı = ",len(hareketlist))
    return hareketlist


def hareketler(islemTarihi,hareketYeri,islem):
    it = []
    hy = []
    isl = []
    for i in islemTarihi.text :
        it.append(i)
    for i in hareketYeri.text :
        hy.append(i)
    for i in islem.text :
        isl.append(i)
    islemTarihi = "".join(it)
    hareketYeri = "".join(hy)
    islem = "".join(isl)
    print("işlem tarihi : ",islemTarihi)
    print("hareket yeri : ",hareketYeri)
    print("islem : ",islem)
   
    return islemTarihi,hareketYeri,islem

def hareketlerHepsijet(islemTarihi,islemVeHareketYeri):
    ithy = []
    it = []
    for i in islemTarihi.text :
        it.append(i)
    for i in islemVeHareketYeri.text :
        ithy.append(i)
    islemVeHareketYeri = "".join(ithy)
    islemTarihi = "".join(it)

    print("işlem tarihi : ",islemTarihi)
    print("islem ve hareket yeri : ",islemVeHareketYeri)
 
   
    return islemTarihi,islemVeHareketYeri
    
def databaseKayitBaslangic (kargoAdi):
    ref = db.reference('/')  
    ref.set({
    kargoAdi:
    {
    }
    })
def datapush (hareketSayisi,list,takipNumarasi,urunSayisi,kargoAdi):
    for hareketNo in range(hareketSayisi):
        ref = db.reference(kargoAdi)
        emp_ref = ref.push({
        'takipNumarasi':takipNumarasi,
        'urunNo':urunSayisi+1,
        'hareketNo':hareketNo+1,
        'islemTarihi':list[hareketNo][0],
        'hareketYeri':list[hareketNo][1],
        'islem':list[hareketNo][2] 
        })
def datapushHepsijet (hareketSayisi,list,takipNumarasi,urunSayisi,kargoAdi):
    for hareketNo in range(hareketSayisi):
        ref = db.reference(kargoAdi)
        emp_ref = ref.push({
        'takipNumarasi':takipNumarasi,
        'urunNo':urunSayisi+1,
        'hareketNo':hareketNo+1,
        'islemTarihi':list[hareketNo][0],
        'islemVeHareketYeri':list[hareketNo][1],
        })
    

def verialma():
    ref = db.reference('suratKargo')
    print(ref.get())


    