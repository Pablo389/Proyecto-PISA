from eq_cuadr import ecuaciones_cuadraticas
from P_PISA import prueba_pisa
from formula_general import formula_general
def main():
    def menu_main():
        print("Ven a aprender matemáticas: ")
        print("Que quieres aprender?: ")
        print("1. Problemas de la prueba PISA")
        print("2. Resolver ecuaciones")
        print("3. Salir del programa")
        while True:
            decision = input()
            try:
                decision = int(decision)
                if decision == 1 or decision ==2 or decision ==3:
                    return decision
                else:
                    print("Por favor ingresa un numero valido")
                    continue
            except:
                print("Por favor ingresa un numero")
                continue
    aciertos = 0
    while True:
        if aciertos >= 20:
            print("Felicidades, estas listo para la prueba")
            break
        ejercicios = menu_main()
        if ejercicios == 1:
            prueba = prueba_pisa()
            aciertos += prueba
        elif ejercicios == 2:
            prueba = formula_general()
            aciertos += prueba
        elif ejercicios == 3:
            print(f"Tus aciertos fueron {aciertos}")
            break
        
    

main()

#Ver si guardamos el puntaje maximo en la base de datos