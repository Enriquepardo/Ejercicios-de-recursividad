import unicodedata

frase = input('Ingrese una frase para saber si es palíndromo: \n')

def reconocer_palindromo(frase):
    frase = ''.join(c for c in frase if c.isalnum())
    frase = ''.join((c for c in unicodedata.normalize('NFD', frase) if unicodedata.category(c) != 'Mn'))
    frase = frase.lower()

    if frase == frase[::-1]:
        print('La frase es palíndromo')
    else:
        print('La frase no es palíndromo')

reconocer_palindromo(frase)
