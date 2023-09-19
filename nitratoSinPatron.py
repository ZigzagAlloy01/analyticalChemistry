import matplotlib.pyplot as plt
import statistics
from math import sqrt

ug = [34.6, 17.3, 13.48, 8.65, 4.325]
abs = [2.116, 1.230, 0.623, 0.317, 0.132]
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
    while round < (ug[0]):
        y = (m * (round)) + (b)
        equationAbs.append(y)
        axisX.append(round)
        round = round + 1.5
    return equationAbs

def drawGraph(list, listTwo, m, b, sm, sb):
    calculusCurve(0, m, b)
    sbPromedio = statistics.stdev(listTwo)
    print(sbPromedio)
    fig = plt.figure(figsize = (12, 7))
    plt.plot(list, listTwo, alpha = 0.4)
    plt.scatter(axisX, equationAbs, color='c', s=40)
    fig.text(0.9, 0.15, f'y = ({m:.4f} ± {sm:.6f} x) + ({b:.4f} ± {sb:.6f})',
         fontsize = 12, color ='black',
         ha ='right', va ='bottom',
         alpha = 0.7)
    fig.text(0.9, 0.15, f'Ensayo realizado a 210 nm.',
         fontsize = 12, color ='black',
         ha ='right', va ='top',
         alpha = 0.7)
    plt.grid(alpha =.6, linestyle ='--')
    plt.title(f'Curva de Calibrado')
    plt.ylabel('Absorbancia')
    plt.xlabel(f'Nitrato de Potasio (ppm)')
    print(equationAbs)
    plt.show()




main()