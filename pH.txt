import math

addHCl = []
addNaOH = []
addBoth = []
addHClW = []
addNaOHW = []
addBothW = []
varianzaSuperiores = []
bucle = 0

def varianzaCalculo(rounds, lista):
    while rounds < n:
        denominador = float((lista[rounds]) - x)
        denominadorDos = denominador **2
        varianzaSuperiores.append(denominadorDos)
        rounds = rounds + 1

while bucle < 5:
    if bucle == 0:
        n = len(addHCl)
        sumatoria = sum(addHCl)
        x = sumatoria/n

        print(' ')
        print(f'El promedio de pH: {x:.4f}. ')

        varianzaCalculo(0, addHCl)
        sumatoriaVarianzaSuperiores = sum(varianzaSuperiores)
        s2 = (sumatoriaVarianzaSuperiores)/(n-1)
    elif bucle == 1:
        n = len(addNaOH)
        sumatoria = sum(addNaOH)
        x = sumatoria/n

        print(' ')
        print(f'El promedio de pH: {x:.4f}. ')

        varianzaCalculo(0, addNaOH)
        sumatoriaVarianzaSuperiores = sum(varianzaSuperiores)
        s2 = (sumatoriaVarianzaSuperiores)/(n-1)
    elif bucle == 2:
        n = len(addBoth)
        sumatoria = sum(addBoth)
        x = sumatoria/n

        print(' ')
        print(f'El promedio de pH: {x:.4f}. ')

        varianzaCalculo(0, addBoth)
        sumatoriaVarianzaSuperiores = sum(varianzaSuperiores)
        s2 = (sumatoriaVarianzaSuperiores)/(n-1)
    elif bucle == 3:
        n = len(addHClW)
        sumatoria = sum(addHClW)
        x = sumatoria/n

        print(' ')
        print(f'El promedio de pH: {x:.4f}. ')

        varianzaCalculo(0, addHClW)
        sumatoriaVarianzaSuperiores = sum(varianzaSuperiores)
        s2 = (sumatoriaVarianzaSuperiores)/(n-1)
    elif bucle == 4:
        n = len(addNaOHW)
        sumatoria = sum(addNaOHW)
        x = sumatoria/n

        print(' ')
        print(f'El promedio de pH: {x:.4f}. ')

        varianzaCalculo(0, addNaOHW)
        sumatoriaVarianzaSuperiores = sum(varianzaSuperiores)
        s2 = (sumatoriaVarianzaSuperiores)/(n-1)
    elif bucle == 5:
        n = len(addBothW)
        sumatoria = sum(addBothW)
        x = sumatoria/n

        print(' ')
        print(f'El promedio de pH: {x:.4f}. ')

        varianzaCalculo(0, addBothW)
        sumatoriaVarianzaSuperiores = sum(varianzaSuperiores)
        s2 = (sumatoriaVarianzaSuperiores)/(n-1)

    print(f'La varianza de las muestras es: {s2:.4f}. ')

    s = math.sqrt(s2)

    print(f'La desviación estándar es: {s:.4f}. ')

    sX = s/(math.sqrt(n))

    print(f'El error estándar es: {sX:.4f}. ')

    cV = (sX/x) * 100

    print(f'El coeficiente de variación es: {cV:.4f}. ')
    print(f'La dispersión de la muestra se ve de la siguiente manera: {x:.2f} ± {s:2f}')
    print(f'Es decir, el intervalo es: {(x - s):.2f} - {(x + s):.2f} ')
    print(f'Si se resta y suma el error estándar, el intervalo es más estrecho: {(x - sX):.2f} - {(x + sX):.2f} ')
    bucle = bucle + 1
    varianzaSuperiores.clear()