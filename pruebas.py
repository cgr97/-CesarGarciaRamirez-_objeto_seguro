import Objeto_Seguro as Fuente

obj1 = Fuente.ObjetoSeguro('Ana') # Creamos objeto Ana
obj2 = Fuente.ObjetoSeguro('David') # Creamos objeto David
t1 = "Hola, soy Ana."
t2 = "Hola, soy David."
t3 = "Vamos por chelas."
t4 = "Jalo."

obj1.gen_llaves()  # Generamos llaves de Ana
obj2.gen_llaves()  # Generamos llaves de David
obj1.intercambio(obj2.nombre, obj2.llave_publica())  # Intercambiamos llaves
obj2.intercambio(obj1.nombre, obj1.llave_publica())  # Intercamiamos llaves
saludo = obj1.saludar(obj1.nombre, t1)  # Objeto1 saluda
obj2.esperar_respuesta(saludo)
respuesta = obj2.responder(t2)
obj1.esperar_respuesta(respuesta)
respuesta2 = obj1.responder(t3)
obj2.esperar_respuesta(respuesta2)
respuesta3 = obj2.responder(t4)
obj1.esperar_respuesta(respuesta3)
obj2.consultar_msj('{ID:<1>}')
obj1.consultar_msj('{ID:<1>}')
obj2.consultar_msj('{ID:<2>}')
obj1.consultar_msj('{ID:<2>}')

