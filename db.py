import sqlite3



def seleccionar_problema(cat, prob):
    conn = sqlite3.connect('preguntas1.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT Nombre_problema FROM Problemas WHERE (Secciones, Problema) = (?,?) ', (cat, prob))
    nombre_prob = cur.fetchone()[0]

    cur.close()
    return nombre_prob

def descripcion_problema(cat, prob):
    conn = sqlite3.connect('preguntas1.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT Descripcion_problema FROM Problemas WHERE (Secciones, Problema) = (?,?) ', (cat, prob))
    nombre_prob = cur.fetchone()[0]

    cur.close()
    return nombre_prob

#Revisar la logica para traer las diferentes preguntas y no solo la primera que aparezca
#Puede ser con un parametro extra, que reciba el numero de pregunta que queremos, y cambiar el fetch
def pregunta(cat, prob, pregu):
    conn = sqlite3.connect('preguntas1.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT Pregunta FROM Preguntas WHERE (Seccion, Problema, Num_preg) = (?,?,?) ', (cat, prob, pregu))
    pregunt = cur.fetchone()[0]

    cur.close()
    return pregunt

def respuestas(cat, prob, pregu):
    conn = sqlite3.connect('preguntas1.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT r1, r2, r3, r4 FROM Preguntas WHERE (Seccion, Problema, Num_preg) = (?,?,?) ', (cat, prob, pregu))
    ans = cur.fetchone()

    cur.close()
    return ans