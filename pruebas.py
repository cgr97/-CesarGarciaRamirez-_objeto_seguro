import Objeto_Seguro_main as f1

ana = f1.ObjetoSeguro('Ana') # Creamos objeto Ana
david = f1.ObjetoSeguro('David') # Creamos objeto David
t1 = "Hola, soy Ana."
t2 = "Hola, soy David."
t3 = "¿Esta conversacion está cifrada?"
t4 = "Lo está."

ana.gen_llaves() # Generamos llaves de Ana
david.gen_llaves() # Generamos llaves de David
llave_ana = ana.llave_publica()  # Obtenemos la llave de Ana
llave_david = david.llave_publica() # Obtenemos la llave de David
ana.intercambio(llave_david)
david.intercambio(llave_ana)
saludo = ana.saludar('Ana',t1)
david.esperar_respuesta(saludo)
respuesta = david.responder(t2)
ana.esperar_respuesta(respuesta)
respuesta2 = ana.responder(t3)
david.esperar_respuesta(respuesta2)
respuesta3 = david.responder(t4)
ana.esperar_respuesta(respuesta3)
david.consultar_msj('{ID:<1>}')
ana.consultar_msj('{ID:<1>}')
david.consultar_msj('{ID:<2>}')
ana.consultar_msj('{ID:<2>}')
