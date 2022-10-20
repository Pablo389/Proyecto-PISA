import random
def ecuaciones_cuadraticas():
    puntos = 0
    print('\nEcuaciones cuadráticas, porfavor redondea tu respuesta a dos decimales')
    print("X1 debe ser positivo y X2 negativo.'")
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    c = random.randint(1, 20)
    print(a,'x^2 ' , ' - ' , b,'x ' , ' - ', c , ' = 0')
    x1_random = (b+(((b**2)-(4*a*(-c)))**0.5))/(2*a)
    x2_random = (b-(((b**2)-(4*a*(-c)))**0.5))/(2*a)
    print(round(x1_random,2), round(x2_random,2))
    while True:
        x1_usuario = input('Cual es X1: ')
        x2_usuario = input('Cual es X2: ')
        try: 
            x2_usuario = float(x2_usuario)
            x1_usuario = float(x1_usuario)
            if x1_usuario == round(x1_random,2) and x2_usuario== round(x2_random,2):
                print('\n¡Estás en lo correcto!')
                puntos += 1
                break
            else:
                print('\nEstás mal, la respuesta correcta es: X1 = ' , round(x1_random,2) ,' y X2 =' , round(x2_random,2))
                return puntos
        except:
            print("Por favor ingresa numeros")
            continue

    return puntos

