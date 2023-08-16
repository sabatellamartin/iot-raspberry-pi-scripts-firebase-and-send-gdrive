import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

PATH_CRED = '/home/pi/Desktop/infinity/iot/service/firebase-key.json'

REF_DISPOSITIVOS = 'dispositivos'
REF_MOTOR = 'motor'
REF_MOVIMIENTO = 'movimiento'
REF_TEMPERATURA = 'temperatura'
REF_DISTANCIA = 'distancia'
REF_CAMARA = 'camara'

class Datos():

    def __init__(self):
        cred = credentials.Certificate(PATH_CRED)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        self.refDispositivos = db.collection(REF_DISPOSITIVOS)
        self.estructuraInicialDB()
        #self.refMotor = self.refDispositivos.child(REF_MOTOR)
        #self.refMovimiento = self.refDispositivos.child(REF_MOVIMIENTO)
        #self.refTemperatura = self.refDispositivos.child(REF_TEMPERATURA)
        #self.refDistancia = self.refDispositivos.child(REF_DISTANCIA)
        #self.refCamara = self.refDispositivos.child(REF_CAMARA)

    def estructuraInicialDB(self):
        self.refDispositivos.document(u'conectados').set({
            'motor': {
                'activo': False,
                'timestamp': 0,
                'tiempo': 1,
                'pasos': 512,
                'sentido': u'horario',
            },
            'movimiento':{
                'activo': False,
                'timestamp': 0
            },
            'temperatura':{
                'activo': False,
                'timestamp': 0,
                'humedad': 0,
                'temperatura': 0
            },
            'distancia':{
                'activo': False,
                'timestamp': 0,
                'centimetros': 0
            },
            'camara':{
                'activo': False,
                'timestamp': 0,
                'capturas': 5,
                'segundos': 5,
                'tipo': u'imagen'
            }
        })

    def obtenerDispositivos(self):
        try:
            doc = self.refDispositivos.document(u'conectados').get()
            #print(u'Document data: {}'.format(doc.to_dict()))
            return doc.to_dict()
        except google.cloud.exceptions.NotFound:
            print(u'No such document!')
            return {}

#    def guardaMovimiento(self, pin, estado, timestamp):
#        self.refStepMotor.document().set({
#            u'timestamp': timestamp,
#            u'estado': estado,
#            u'pin': pin
#        })
