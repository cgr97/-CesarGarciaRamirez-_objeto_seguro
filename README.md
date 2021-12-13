# -CesarGarciaRamirez-_objeto_seguro
Esta es la forma en que funciona mi código: 

import Objeto_Seguro as Fuente

obj1 = Fuente.ObjetoSeguro('Ana') # Creamos objeto Ana
obj2 = Fuente.ObjetoSeguro('David') # Creamos objeto David
t1 = "Hola, soy Ana."
t2 = "Hola, soy David."
t3 = "Esta es una conversacion segura."
t4 = "Si es."

obj1.gen_llaves()  # Generamos llaves de Ana
obj2.gen_llaves()  # Generamos llaves de David
obj1.intercambio(obj2.nombre, obj2.llave_publica())  # Intercambiamos llaves
obj2.intercambio(obj1.nombre, obj1.llave_publica())  # Intercamiamos llaves
saludo = obj1.saludar(obj1.nombre, t1)  # Ana saluda con mensaje cifrado
obj2.esperar_respuesta(saludo)  # David espera la respuesta y la descifra 
respuesta = obj2.responder(t2)  # David responde con mensaje cifrado
obj1.esperar_respuesta(respuesta)  
respuesta2 = obj1.responder(t3)
obj2.esperar_respuesta(respuesta2)
respuesta3 = obj2.responder(t4)
obj1.esperar_respuesta(respuesta3)
obj2.consultar_msj('{ID:<1>}')  # David busca en su registro
obj1.consultar_msj('{ID:<1>}')  # Ana busca en su registro
obj2.consultar_msj('{ID:<2>}')
obj1.consultar_msj('{ID:<2>}')

Este programa, primero, instancia dos objetos de la clase ObjetoSeguro, y creando 4 mensajes predeterminados. Después, los objetos generan sus llaves publicas y privadas y las intercambian junto con su nombre para que el otro pueda conocer su llave publica y pueda cifrar mensajes con ella. Así, uno de los objetos saluda, en ese proceso se codifica y cifra un mensaje. El otro objeto recibe espera a la respuesta y descifra y decodifica el mensaje. Ahora el objeto 2 responde con mensaje cifrado y asi intercambian 4 mensajes. Posteriormente, los objetos consultan sus registros de mensajes descifrados. 

