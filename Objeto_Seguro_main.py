import json
from ecies.utils import generate_eth_key
from ecies import encrypt, decrypt
import binascii
import base64


class ObjetoSeguro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.llave_pub = 0
        self.llave_priv = 0
        self.otrallave = 0
        self.otronombre = 0
        self.id = 0
        self.registro = {}

    def intercambio(self,llave):
        self.otrallave = llave[0] # Guarda la llave publica
        self.otronombre = llave[1] # Guarda el nombre
        print(self.nombre+": Intercambio Exitoso")

    def gen_llaves(self):
        llavepriv = generate_eth_key()  # Genera la llave privada
        self.llave_priv = llavepriv.to_hex()  # Pasa la llave privada a str
        self.llave_pub = llavepriv.public_key.to_hex()  # Genera la llave publica en str

    def saludar(self,name,msj):
        codificado = self.codificar64(msj) # Recibe en texto plano y saca el msj en bytes
        cifrado = self.cifrar_msj(self.otrallave,codificado) # Recibe en bytes y saca el msj en formato llave
        print(f'{name}{": "}{cifrado}')
        return cifrado # Devuelve un mensaje tipo llave

    def responder(self,msj):
        codificado = self.codificar64(msj)  # Recibe en texto plano y saca el msj en bytes
        cifrado = self.cifrar_msj(self.otrallave, codificado)  # Recibe en bytes y saca el msj en formato llave
        print("MensajeRespuesta "+cifrado)
        return cifrado # Devuelbe un mensaje tipo llave

    def llave_publica(self):
        print(self.nombre+": "+"mi llave publica es "+self.llave_pub)
        return self.llave_pub,self.nombre  # Retorna la llave publica

    def cifrar_msj(self, pub_key, msj):
        msjb = msj.encode() # Convierte el msj de str a bytes
        cifradollave = encrypt(pub_key, msjb)  # Cifra con la publica y el mensaje en bytes
        cifradob = binascii.hexlify(cifradollave)
        cifrado = cifradob.decode() # Decodifica cifradob de bytes a str
        # print(self.nombre+" cifra "+cifrado)
        return cifrado

    def descifrar_msj(self, msj):
        msjb = msj.encode()
        msjllave = binascii.a2b_hex(msjb)
        descifradollave = decrypt(self.llave_priv, msjllave)  # Descifra con la privada y el mensaje en bytes
        descifrado = descifradollave.decode()
        # print(self.nombre+" descifra "+descifrado)
        return descifrado # Saca el saje en bytes

    def codificar64(self, msj):
        msjb = msj.encode()  # Codifica msj de str a byte
        codificado = base64.b64encode(msjb)  # Codifica msjb en base64
        msjnb = codificado.decode()  # Decodifica codemsj de bytes a str
        # print(self.nombre+" codifica "+msjnb)
        return msjnb

    def decodificar64(self, msj):
        msjb = msj.encode()
        decodificadob = base64.b64decode(msjb)  # Decodifica de base64
        decodificado = decodificadob.decode()  # Decodifica de byte a str
        # print(decodificado)
        return decodificado # Retorna bytes

    def almacenar_msj(self,msj):
        self.id = int(self.id)
        self.id = self.id + 1
        nombrearchivo = "RegistoMsj_<"+self.nombre+">.json"
        self.registro.update({
            "ID:<"+str(self.id)+">": msj})
        print(self.registro)
        with open(nombrearchivo, 'w') as f:
            json.dump(self.registro, f, indent=4)
        self.id = str(self.id)
        print("ID:<"+self.id+">")
        return "{ID:<"+self.id+">}"

    # def consultar_msj(self,id):
    def esperar_respuesta(self,msj):
        descifrado = self.descifrar_msj(msj) # Descifra con la privada y el msj en tipo llave
        decodificado = self.decodificar64(descifrado) # Decodifica con el mensaje en bytes
        # print(self.nombre+": recibí "+decodificado)
        self.almacenar_msj(decodificado)


# print('Creamos objeto')
# nombre = 'Cesar'
# obj = ObjetoSeguro(nombre)
# print('Generamos llaves')
# obj.gen_llaves()
# print('Obtenemos llave publica')
# publica = obj.llave_publica()
# TextoPlano = "********** Este es un mensaje de prueba que no debe leerse **********"
# print('Codificamos:',TextoPlano)
# codificado = obj.codificar64(TextoPlano)
# print('Ciframos')
# cifrado = obj.cifrar_msj(publica, codificado)
# print('Saludamos')
# obj.saludar(nombre,cifrado)
# print('Desciframos')
# descifrado = obj.descifrar_msj(cifrado)
# print('Decodificamos')
# decodificado = obj.decodificar64(descifrado)


