import math

def area_circulo(raio):
    return math.pi * (raio ** 2)

raio = float(input('Informe o raio: '))
print(f'Área do círculo: {area_circulo(raio)}')
