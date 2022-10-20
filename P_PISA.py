#Reto problemas PISA Matemáticas
#Pablo Heredia A01637103
import db
import random 

secciones = ["1.Aritmética","2.Geometría","3.Funciones y gráficas","4.Estadística descriptiva", "5.Salir del programa"]
categorias = {
    1 : ["1.Chatear", "2.Concierto de Rock", "3.El Tipo de Cambio", "4.Cambio Por Superficie", "5.Frecuencia De Goteo"],
    2 : ["1.El Patio", "2.Pizzas", "3.Vuelo Espacial", "4.Barcos De Vela", "5.Puerta Giratoria"],
    3 : ["1.El sueño de las focas", "2.Latidos del corazon"],
    4 : ["1.Estatura de los alumnos", "2. Examen de ciencias", "3.Estatura"],
}
#esta funcion devuelve que sección es la que quiere trabajar el usuario, a partir de la lista secciones
def menu_secciones(secc):
    print("Elige una de las siguientes secciones (Ingresa solo el numero): ")
    for element in secc:
        print(element)
    while True:
        seccion = input()
        try:
            seccion = int(seccion)
            if seccion not in range(1,6):
                continue
            else:
                return seccion
        except:
            continue
#Esta funcion devuelve el problema que quiere trabajar el usuario, a partir de
# el diccionario de categorias     
def menu_problemas(indice):
    print(f"Bienvenido a {secciones[indice-1]}, por favor selecciona un problema")
    categoria = categorias[indice]
    for element in categoria:
        print(element)
    x = len(categoria)+1
    print(f"{x}.Regresar al menu principal")
    while True:
        problema = input()
        try:
            problema = int(problema)
            if problema == x:
                return "Regresar"
            if problema not in range(1, len(categoria)+1):
                continue
            else:
                return problema
        except:
            continue
    
#Esta funcion muestra el problema que selecciona el ususario accedienco a un archivo .txt
def mostrar_problema(cate, proble):
    nombre_problema = db.seleccionar_problema(cate, proble)
    print(nombre_problema)
    #descripcion_prob = db.descripcion_problema(cate, proble)
    desc_prob = open(f"txts/{str(nombre_problema)}.txt", "r", encoding="utf-8")
    print(desc_prob.read())
    desc_prob.close()
    
#esta funcion muestra la pregunta correspondiente al problema y nivel que esta el usuario
#sacando el texto de un archivo txt
def mostrar_pregunta(cate, proble, preg):
    pregunta_prob = db.seleccionar_problema(cate, proble)
    pregunta_open = open(f"txts/{str(pregunta_prob)}{preg}.txt", "r", encoding="utf-8")
    print(pregunta_open.read())
    pregunta_open.close()

#Esta función valida si la respuesta abierta ingresada concuerda con nuestra base de datos
def validar_respuesta_abierta(cate, proble, preg):
    respuesta_abierta = db.respuestas(cate, proble, preg)
    respuesta_abierta = list(respuesta_abierta)
    correcto = respuesta_abierta[0]
    while True:
        resp_usuario = input("Ingresa la respuesta: ")
        try:
            #resp_usuario = int(resp_usuario)
            if resp_usuario == correcto:
                print("Estas en lo correcto")
                return True
            else:
                print("mal")
                return False
        except:
            print("Por favor ingresa un numero")
            continue

#muestra las respuestas a la pregunta que selecciona el usuario, y devuelve dos listas
#una con las respuestas ordenadas y otra sorteadas, siempre la respuesta correcta será la primera de 
#la lista ordenada
def mostrar_respuestas_multiple(cate, proble, preg):
    respuesta_lista = db.respuestas(cate, proble, preg)
    respuesta_lista = list(respuesta_lista)
    revueltas = random.sample(respuesta_lista, len(respuesta_lista))
    print("Cual es la respuesta correcta? (Ingresa el numero)")
    x = 1
    for element in revueltas:
        print(f"{x}. {element}")
        x += 1
    return respuesta_lista, revueltas
#esta función pide y valida la respuesta ingresada por el usuario en base a las listas de mostrar_respuestas
def validar_respuesta_multiple(listas):
    original, rev = listas
    while True:
        respuesta = input()
        try: 
            respuesta = int(respuesta)
            if rev[respuesta-1] == original[0]:
                print("Estas en lo correcto")
                return True
            else:
                print("mal")
                return False
        except:
            continue

#Muestra el problema, y valida las respuestas usando otras funciones
def most_prob_resp(cate, proble):
    mostrar_problema(cate, proble)
    #En un futuro poner un ciclo para ver cuantas preguntas va a responder el usuario, accediendo desde la db
    mostrar_pregunta(cate, proble, 1)
    print(db.respuestas(cate,proble,1))
    if list(db.respuestas(cate,proble,1))[1] == "":
        acierto = validar_respuesta_abierta(cate, proble, 1)
    else:
        resp = mostrar_respuestas_multiple(cate, proble, 1)
        acierto = validar_respuesta_multiple(resp)
    return acierto

def prueba_pisa():
    correctas = 0
    while True:
        print("Correctas: ", correctas)
        categoria = menu_secciones(secciones)
        if categoria == 5:
            return correctas
        problemaEleg = menu_problemas(categoria)
        if problemaEleg == "Regresar":
            continue
        atino = most_prob_resp(categoria, problemaEleg)
        if atino:
            correctas += 1
        if correctas == 20:
            return correctas
            

