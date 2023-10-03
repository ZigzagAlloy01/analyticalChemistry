import matplotlib.pyplot as plt
import statistics
from math import sqrt
#Para 40 mM fueron 1.811 de abs
mM = [20, 10, 5, 2.5, 1.25, 0.625]
abs = [1.785, 1.511, 1.123, 1.058, 0.811, 0.337]
xyValues = []
xSquareValues = []
dSquareValues = []
equationAbs = []
axisX = []

def main():
    n = len(abs) 
    ΣX = sum(mM)
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
    return drawGraph(mM, abs, m, b, sm, sb)

def calculusXY(round):
    while round < (len(mM)):
        xy = (mM[round]) * (abs[round])
        xyValues.append(xy)
        round = round + 1
    xySumatory = sum(xyValues)
    return xySumatory

def calculusXSquare(round):
    while round < (len(mM)):
        xSquare = (mM[round])**2
        xSquareValues.append(xSquare)
        round = round + 1
    xSquareSumatory = sum(xSquareValues)
    return xSquareSumatory

def calculusDSquare(round, m, b):
    while round < (len(mM)):
        dValue = (abs[round]) - (m * (mM[round])) - b
        dSquare = dValue ** 2
        dSquareValues.append(dSquare)
        round = round + 1
    dSquareSumatory = sum(dSquareValues)
    return dSquareSumatory

def calculusCurve(round, m, b):
    while round < mM[0]:
        y = (m * (round)) + (b)
        equationAbs.append(y)
        axisX.append(round)
        round = round + (mM[0] * 0.03)
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
    plt.title(f'Curva de Calibración')
    plt.ylabel('Absorbancia')
    plt.xlabel(f'Glucosa (mM)')
    print(equationAbs)
    plt.show()

main()