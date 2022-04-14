import pyrebase 
from config import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def get_rfb():
    return db.child("YOT").get().val()

def update_first(message):
    db.child("YOT").update({
        "word1": message
    })

def update_second(message):
    db.child("YOT").update({
        "word2": message
    })

def update_third(message):
    db.child("YOT").update({
        "word3": message
    })

