from random import randint
def formula_general():
    status='si'
    acc=0
    while status=='si':
        val_a=randint(1,5)
        val_b=randint(-9,9)
        val_c=randint(-9,9)
        while ((val_b**2)-(4*val_a*val_c))<0:
            val_b+=1
        x1=(-val_b+((val_b**2)-(4*val_a*val_c))*0.5)/(2*val_a)
        x2=(-val_b-((val_b**2)-(4*val_a*val_c))*0.5)/(2*val_a)
        x1=round(x1,2)
        x2=round(x2,2)
        print(f'Realiza la siguiente ecuación cuadratica mediante la fórmula general\n{val_a}x²+({val_b})x+({val_c})=0')
        print(x1,x2)
        validador=0
        while validador==0:
            try:
                respuesta1 = float(input('¿Cuanto vale x1? (Redondea a 2 decimales)\n:'))
                respuesta2 = float(input('¿Cuánto vale x2? (Redondea a 2 decimales)\n:'))
                validador+=1
            except ValueError:
                print("Valor invalido, intentalo de nuevo")
        if respuesta1 == x1 and respuesta2 == x2:
            acc+=1
            status=str(input("Correcto! +1 punto, ¿deseas intentar una nueva ecuación? (Escribe si para continuar)\n"))
            status.lower()
        else:
            seguir=''
            while respuesta1 != x1 or respuesta2 != x2 or seguir=='si':
                seguir=str(input("Incorrecto, ¿deseas intentarlo de nuevo? (Escribe si para continuar)\n"))
                seguir.lower()
                if seguir=='si':
                    validador=0
                    while validador==0:
                        try:
                            respuesta1 = float(input('¿Cuanto vale x1? (Redondea a 2 decimales)\n:'))
                            respuesta2 = float(input('¿Cuánto vale x2? (Redondea a 2 decimales)\n:'))
                            validador+=1
                        except ValueError:
                            print("Valor invalido, intentalo de nuevo")
                    if respuesta1 == x1 and respuesta2 == x2:
                        acc+=1
                        seguir=''
                        status=str(input("Correcto! +1 punto, ¿deseas intentar una nueva ecuación? (Escribe si para continuar)\n"))
                        status.lower()
                else:
                    respuesta1=x1
                    respuesta2=x2
                    status=str(input("¿Deseas intentar una nueva ecuación? (Escribe si para continuar)\n"))
                    status.lower()
    return acc
