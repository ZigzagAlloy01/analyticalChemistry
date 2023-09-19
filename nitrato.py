moles = 0.00685
pm = 101.1

ppm = (moles * pm) * 1000
nitratoPotasio = []
nitratoSolo = []
nitrogenoSolo = []
multiplicador = [0.6, 0.4, 0.2, 0.1, 0.02, 0]
print(f'Las partes por millon de Nitrato de Potasio son: {ppm:.2f}')

rounds = 0
tubos = 6
nitratoPotasio.append(ppm)
while rounds < tubos:
    ppm = (moles * pm) * 1000
    ppm = ppm*(multiplicador[rounds])
    rounds = rounds + 1
    nitratoPotasio.append(ppm)
print(nitratoPotasio)

pm = 62
ppm = (moles * pm) * 1000
print(f'Las partes por millon de Nitrato son: {ppm:.2f}')

rounds = 0
nitratoSolo.append(ppm)
while rounds < tubos:
    ppm = (moles * pm) * 1000
    ppm = ppm*(multiplicador[rounds])
    rounds = rounds + 1
    nitratoSolo.append(ppm)
print(nitratoSolo)

pm = 14
ppm = (moles * pm) * 1000
print(f'Las partes por millon de Nitrogeno son: {ppm:.2f}')

rounds = 0
nitrogenoSolo.append(ppm)
while rounds < tubos:
    ppm = (moles * pm) * 1000
    ppm = ppm*(multiplicador[rounds])
    rounds = rounds + 1
    nitrogenoSolo.append(ppm)
print(nitrogenoSolo)

