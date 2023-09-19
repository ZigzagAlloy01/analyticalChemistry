import matplotlib.pyplot as plt
import statistics
from math import sqrt

ug = [0.2, 0.1, 0.05, 0.025, 0.0125]
abs = [0.926, 0.4435, 0.2675, 0.1275, 0.065]
absPuntoCeroDos = [0.096, 0.096, 0.092, 0.092, 0.092]
absPuntoCeroOcho = [0.242, 0.259, 0.243, 0.251, 0.226]
xyValues = []
xSquareValues = []
dSquareValues = []
equationAbs = []
axisX = []

def main():
    n = len(abs) 
    ΣX = sum(ug)
    ΣY  = sum(abs)
    ΣXY  = calculusXY(0)
    ΣXSquare = calculusXSquare(0)
    determinant = ((n) * (ΣXSquare)) - ((ΣX * ΣX))
    m = ((ΣXY * n) - (ΣX * ΣY)) / determinant
    b = ((ΣXSquare * ΣY) - (ΣXY * ΣX)) / determinant
    ΣDSquare = calculusDSquare(0, m, b)
    sY = sqrt(ΣDSquare/(n-2))
    s2m = ((sY**2) * n) / determinant
    s2b = ((sY**2) * ΣXSquare) / determinant
    sm = sqrt(s2m)
    sb = sqrt(s2b)
    print(f'La ecuación de la recta es: y = ({m:.4f} ± {sm:.6f} x) + ({b:.4f} ± {sb:.6f})')
    find = 0.973
    secret = (find - b) / m
    print(f'La masa de la muestra problema, con absorbancia de {find} es de: {secret:.4f} µg.')
    return drawGraph(ug, abs, m, b, sm, sb)

def calculusXY(round):
    while round < (len(ug)):
        xy = (ug[round]) * (abs[round])
        xyValues.append(xy)
        round = round + 1
    xySumatory = sum(xyValues)
    return xySumatory

def calculusXSquare(round):
    while round < (len(ug)):
        xSquare = (ug[round])**2
        xSquareValues.append(xSquare)
        round = round + 1
    xSquareSumatory = sum(xSquareValues)
    return xSquareSumatory

def calculusDSquare(round, m, b):
    while round < (len(ug)):
        dValue = (abs[round]) - (m * (ug[round])) - b
        dSquare = dValue ** 2
        dSquareValues.append(dSquare)
        round = round + 1
    dSquareSumatory = sum(dSquareValues)
    return dSquareSumatory

def calculusCurve(round, m, b):
    while round < 0.36:
        y = (m * (round)) + (b)
        equationAbs.append(y)
        axisX.append(round)
        round = round + 0.04
    return equationAbs

def drawGraph(list, listTwo, m, b, sm, sb):
    calculusCurve(0, m, b)
    sbPromedio = statistics.stdev(listTwo)
    print(sbPromedio)
    sbPromedio1 = statistics.stdev(absPuntoCeroDos)
    print(sbPromedio1)
    sbPromedio2 = statistics.stdev(absPuntoCeroOcho)
    print(sbPromedio2)
    smNuevo = ((b)/2) + (3 * sbPromedio1)
    cM = (smNuevo - sbPromedio1) / m 
    smNuevo = ((b)/2) + (3 * sbPromedio2)
    cM2 = (smNuevo - sbPromedio2) / m 
    fig = plt.figure(figsize = (12, 7))
    plt.plot(list, listTwo, alpha = 0.4)
    plt.scatter(list, listTwo, color='c', s=40)
    fig.text(0.9, 0.15, f'y = ({m:.4f} ± {sm:.6f} x) + ({b:.4f} ± {sb:.6f})',
         fontsize = 12, color ='black',
         ha ='right', va ='bottom',
         alpha = 0.7)
    fig.text(0.9, 0.15, f'Ensayo realizado a 520 nm. Cm1 = {cM:.4f} M Cm2 = {cM2:.4f} M',
         fontsize = 12, color ='black',
         ha ='right', va ='top',
         alpha = 0.7)
    plt.grid(alpha =.6, linestyle ='--')
    plt.title(f'Curva de Calibrado')
    plt.ylabel('Absorbancia')
    plt.xlabel(f'Cobalto analizado (M)')
    print(equationAbs)
    plt.show()




main()