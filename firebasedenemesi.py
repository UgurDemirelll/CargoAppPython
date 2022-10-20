
import pyrebase

firebaseConfig = {'apiKey': "AIzaSyClIWeT-uwCWfy1c9WXxjjRr60pcDoVXQ0",
  'authDomain': "cargo-964c3.firebaseapp.com",
  'databaseURL': "https://cargo-964c3-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "cargo-964c3",
  'storageBucket': "cargo-964c3.appspot.com",
  'messagingSenderId': "37575557630",
  'appId': "1:37575557630:web:05be24e89637057284c0af"}


def firebasedenIdListesiAl():
    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    kargoList = ["hepsijet","mngKargo","pttKargo","suratKargo"]
    firebaseIdList = []
    for kargo in kargoList:
        liste = db.child(kargo).get().val()
        for i in liste:
            id = i
            aralist = [id,kargo]
            firebaseIdList.append(aralist)
            print("id: ",id)
    return firebaseIdList



