molar = [0, 2, 4, 6, 8, 10]
abs = [0.002, 0.15, 0.294, 0.434, 0.57, 0.704]
multiplicacionXY = []
cuadradoX = []

Σx = sum(molar)
Σy = sum(abs)
def determinante(a, b, c):
    d = ((a*c) - (b*b))
    return d

def pendiente(a, b, c, d, e):
    m = ((a*b) - (c*d)) / e
    return m

round = 0
while round < (len(molar)):
    parametro1 = (molar[round]) * (abs[round])
    multiplicacionXY.append(parametro1)
    round = round + 1
print(multiplicacionXY)
Σxy = sum(multiplicacionXY)

round = 0
while round < (len(molar)):
    parametro2 = (molar[round])**2
    cuadradoX.append(parametro2)
    round = round + 1
print(cuadradoX)
Σx2 = sum(cuadradoX)

n = len(molar)
d = determinante(Σx2, Σx, n)
m = pendiente(Σxy, n, Σx, Σy, d)
print(m)