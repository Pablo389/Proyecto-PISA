from random import randint as rd


#este es mi coigo de prueba por si quiero hacer algo mas elaborado

#FAVOR DE BORRAR SI NO SE VA A USAR
def discriminante(a,b,c):
    disc = (b**2)-4*a*c
    if disc >0:
        return True
    elif disc <=0:
        return False

def crear_coeficientes():
    while True:
        a = rd(-9,9)
        b = rd(-9,9)
        c = rd(-9,9)
        if a == 0 or b == 0 or c==0:
            continue
        else:
            if discriminante(a,b,c):
                return a,b,c
            else:
                continue

def ecuacion_cuad():
    a,b,c = crear_coeficientes()
    x1=(-b+((b**2)-(4*a*c))*0.5)/(2*a)
    x2=(-b-((b**2)-(4*a*c))*0.5)/(2*a)
    x1=round(x1,2)
    x2=round(x2,2)
    print(f'Realiza la siguiente ecuación cuadratica mediante la fórmula general\n{a}x²+{b}x+{c}')
    respuesta1 = float(input('¿Cuanto vale x1? (Redondea a 2 decimales)\n:'))
    respuesta2 = float(input('¿Cuánto vale x2? (Redondea a 2 decimales)\n:'))
