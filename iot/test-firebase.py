import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("/service/firebase-key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

tests_ref = db.collection(u'tests')
docs = tests_ref.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
