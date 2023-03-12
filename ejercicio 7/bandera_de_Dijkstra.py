import random

fichas = ['R', 'V', 'A']
a = int(input('Ingrese la cantidad de fichas: '))


def decorador(funcion):
    def wrapper():
        print('Fichas mezcladas: ', funcion())
    return wrapper

@decorador
def mezclar_fichas():
    for i in range(a):
        fichas.append(random.choice(fichas))
    return fichas


def ordenar_fichas():
    n = len(fichas)
    i = 0  
    j = 0  
    k = n-1  
    while j <= k:
        if fichas[j] == 'R':
            fichas[i], fichas[j] = fichas[j], fichas[i]
            i += 1
            j += 1
        elif fichas[j] == 'V':
            j += 1
        else:
            fichas[j], fichas[k] = fichas[k], fichas[j]
            k -= 1
    return fichas

def main():
    mezclar_fichas()
    print(ordenar_fichas())


main()
