import socket
from concurrent.futures import ThreadPoolExecutor
import Objeto_Seguro


class Socket:
    def __init__(self):
        self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port_and_ip = ('127.0.0.1', 12363)

    def iniciar_cliente(self,eleccion):
        self.node.connect(self.port_and_ip)
        self.mandarllave(eleccion)
        self.guardarllave(eleccion)
        self.mandarnombre(eleccion)
        self.guardarnombre(eleccion)
        with ThreadPoolExecutor(max_workers=2) as executor:
            mandar = executor.submit(self.sender(eleccion), 1)
            recibir = executor.submit(self.receiver(eleccion), 2)

    def iniciar_servidor(self,eleccion):
        self.node.bind(self.port_and_ip)
        self.node.listen(10)
        self.node.setblocking(False)
        with ThreadPoolExecutor(max_workers=3) as executor:
            aceptar = executor.submit(self.aceptar(), 1)
            recibir = executor.submit(self.receiver(eleccion), 2)
            mandar = executor.submit(self.sender(eleccion), 3)

    def aceptar(self):
        print("aceptar iniciado")
        while True:
            try:
                self.connection, addr = self.node.accept()
                self.node.setblocking(False)
                self.guardarllave(eleccion)
                self.mandarllave(eleccion)
                self.guardarnombre(eleccion)
                self.mandarnombre(eleccion)
                break
            except:
                pass

    def receiver(self, eleccion):
        if eleccion == "C":
            while True:
                msgc = self.node.recv(1024).decode()
                msg = self.objetoseguro.esperar_respuesta(msgc)
                print(f"<<< {msg}")
                return
        elif eleccion == "S":
            msgc = self.connection.recv(1028).decode()
            msg = self.objetoseguro.esperar_respuesta(msgc)
            while msg != "exit":
                print(f"<<< {msg}")
                return
            print("Adios")
            self.connection.close()
            exit()

    def send_sms(self, SMS, eleccion):
        if eleccion == "C":
            self.node.send(SMS)
        elif eleccion == "S":
            self.connection.send(SMS)

    def sender(self, eleccion):
        if eleccion == "C":
            message = input(">>> ")
            cmessage = self.objetoseguro.responder(message)
            while message != "exit":
                self.send_sms(cmessage, eleccion)
                return
            self.send_sms(cmessage, eleccion)
            print("Adios")
            self.node.close()
            exit()
        elif eleccion == "S":
            while True:
                message = input(">>> ")
                cmessage = self.objetoseguro.responder(message)
                self.send_sms(cmessage, eleccion)
                return

    def genobjetoseguro(self, nombre):
        self.objetoseguro = Objeto_Seguro.ObjetoSeguro(nombre)

    def mandarllave(self, eleccion):
        if eleccion == "C":
            llave = self.objetoseguro.llave_publica().encode()
            self.send_sms(llave, eleccion)
            return llave
        elif eleccion == "S":
            llave = self.objetoseguro.llave_publica().encode()
            self.send_sms(llave, eleccion)
            return llave

    def mandarnombre(self, eleccion):
        if eleccion == "C":
            nombre = self.objetoseguro.nombre.encode()
            self.send_sms(nombre, eleccion)
            return nombre
        elif eleccion == "S":
            nombre = self.objetoseguro.nombre.encode()
            self.send_sms(nombre, eleccion)
            return nombre

    def guardarllave(self, eleccion):
        if eleccion == "C":
            otrallave = self.node.recv(1024).decode()
            self.objetoseguro.otrallave = otrallave
        elif eleccion == "S":
            otrallave = self.connection.recv(1024).decode()
            self.objetoseguro.otrallave = otrallave

    def guardarnombre(self, eleccion):
        if eleccion == "C":
            otronombre = self.node.recv(1024).decode()
            self.objetoseguro.otronombre = otronombre
        elif eleccion == "S":
            otronombre = self.connection.recv(1024).decode()
            self.objetoseguro.otronombre = otronombre


if __name__ == '__main__':
    eleccion = input("¿Cual es mi funcion S/C? ")
    nombre = input("¿Cual es mi nombre? ")
    s = Socket()
    s.genobjetoseguro(nombre)
    s.objetoseguro.gen_llaves()
    print(s.objetoseguro.nombre)
    if eleccion == "C":
        print("Modo cliente")
        s.iniciar_cliente("C")
        while True:
            s.sender(eleccion)
            s.receiver(eleccion)
            continue
    elif eleccion == "S":
        print("Modo Servidor")
        s.iniciar_servidor("S")
        while True:
            s.receiver(eleccion)
            s.sender(eleccion)
            continue