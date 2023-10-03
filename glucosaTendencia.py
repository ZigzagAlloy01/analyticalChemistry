import matplotlib.pyplot as plt
import statistics
from math import sqrt

ug = [40, 20, 10, 5, 2.5, 1.25, 0.625, 0.3125]
abs = [1.115, 0.88, 0.377, 0.306, 0.205, 0.15, 0.046, 0.012]
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
    #print(f'La masa de la muestra problema, con absorbancia de {find} es de: {secret:.4f} µg.')
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
        round = round + (ug[0] * 0.04)
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
    fig.text(0.9, 0.15, f'Ensayo realizado a 540 nm.',
         fontsize = 12, color ='black',
         ha ='right', va ='top',
         alpha = 0.7)
    plt.grid(alpha =.6, linestyle ='--')
    plt.title(f'Curva de Calibracion')
    plt.ylabel('Absorbancia')
    plt.xlabel(f'Glucosa (mM)')
    print(equationAbs)
    plt.show()




main()