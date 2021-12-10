import json
from ecies.utils import generate_eth_key
from ecies import encrypt, decrypt
import binascii
import base64


class ObjetoSeguro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__llave_pub = 0
        self.__llave_priv = 0
        self.__otrallave = 0
        self.__otronombre = 0
        self.__id = 0
        self.__registro = {}

    def intercambio(self, nombre, llave):
        self.__otronombre = nombre  # Guarda la llave publica
        self.__otrallave = llave  # Guarda el nombre
        print(self.nombre + ": Intercambio Exitoso")

    def gen_llaves(self):
        llavepriv = generate_eth_key()  # Genera la llave privada
        self.__llave_priv = llavepriv.to_hex()  # Pasa la llave privada a str
        self.__llave_pub = llavepriv.public_key.to_hex()  # Genera la llave publica en str

    def saludar(self, name, msj):
        codificado = self.__codificar64(msj)  # Recibe en texto plano y saca el msj en bytes
        cifrado = self.__cifrar_msj(self.__otrallave, codificado)  # Recibe en bytes y saca el msj en formato llave
        print(f'{name}{" saluda: "}{cifrado}')
        return cifrado  # Devuelve un mensaje tipo llave

    def responder(self, msj):
        codificado = self.__codificar64(msj)  # Recibe en texto plano y saca el msj en bytes
        cifrado = self.__cifrar_msj(self.__otrallave, codificado)  # Recibe en bytes y saca el msj en formato llave
        print("MensajeRespuesta " + cifrado)
        return cifrado  # Devuelbe un mensaje tipo llave

    def llave_publica(self):
        print(self.nombre + ": " + "mi llave publica es " + self.__llave_pub)
        return self.__llave_pub  # Retorna la llave publica

    @staticmethod
    def __cifrar_msj(pub_key, msj):
        msjb = msj.encode()  # Convierte el msj de str a bytes
        cifradollave = encrypt(pub_key, msjb)  # Cifra con la publica y el mensaje en bytes
        cifradob = binascii.hexlify(cifradollave)
        cifrado = cifradob.decode()  # Decodifica cifradob de bytes a str
        return cifrado

    def __descifrar_msj(self, msj):
        msjb = msj.encode()
        msjllave = binascii.a2b_hex(msjb)
        descifradollave = decrypt(str(self.__llave_priv), msjllave)  # Descifra con la privada y el mensaje en bytes
        descifrado = descifradollave.decode()
        return descifrado  # Saca el saje en bytes

    @staticmethod
    def __codificar64(msj):
        msjb = msj.encode()  # Codifica msj de str a byte
        codificado = base64.b64encode(msjb)  # Codifica msjb en base64
        msjnb = codificado.decode()  # Decodifica codemsj de bytes a str
        return msjnb

    @staticmethod
    def __decodificar64(msj):
        msjb = msj.encode()
        decodificadob = base64.b64decode(msjb)  # Decodifica de base64
        decodificado = decodificadob.decode()  # Decodifica de byte a str
        return decodificado  # Retorna str

    def __almacenar_msj(self, msj):
        self.__id = int(self.__id)
        self.__id = self.__id + 1
        nombrearchivo = "RegistoMsj_<" + self.nombre + ">.json"
        idstr = str(self.__id)
        self.__registro["{ID:<" + idstr + ">}"] = {
            'ID': self.__id,
            'REGISTRA': self.nombre,
            'MSJ': msj,
            'Fuente': self.__otronombre}
        with open(nombrearchivo, 'w') as f:
            json.dump(self.__registro, f, indent=4)
        print("{ID:<" + idstr + ">}")
        return "{ID:<" + idstr + ">}"

    def consultar_msj(self, id):
        nombrearchivo = "RegistoMsj_<" + self.nombre + ">.json"
        with open(nombrearchivo, 'r') as consulta:
            objeto_json = json.load(consulta)
            print(objeto_json[str(id)])
        return objeto_json[str(id)]

    def esperar_respuesta(self, msj):
        descifrado = self.__descifrar_msj(msj)  # Descifra con la privada y el msj en tipo llave
        decodificado = self.__decodificar64(descifrado)  # Decodifica con el mensaje en bytes
        self.__almacenar_msj(decodificado)
