uA1 = 2.36
uA2 = 3.79
v1 = 20
v2 = 20.5
c2 = 0.0287

#factor para [Ni]i : [Ni]i (20/20.5)
#factor para [Ni]i : 0.0287 M (0.5/20.5)


uA3 = uA1/uA2
factor = c2 * (0.5/20.5)
despejeUno = (0.0007 * uA3)
despejeDos = (factor * uA3)
NiInicial = despejeUno / (1 - despejeDos)
NiFinal = 0.0007 + NiInicial 
print('La expresión de la concentración de niquel es: [Ni]i / [0.0007 M] + 0.9756[Ni]i) = 2.36 µA / 3.79 µA)')
print(f'La [Ni]i en la muestra problema de 20 mL era de: {NiInicial:.4f} M. ')
print(f'La concentración final de níquel en disolución fue de: {NiFinal:.4f} M. ')