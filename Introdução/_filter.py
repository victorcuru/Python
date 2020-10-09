'''
    - Utilizando o método filter e 'filtrando' apenas os valores pares de uma lista a partir de
    um range de valores entre 0 e 100
'''
#lista = list(range(0, 100))

numeros_pares = list(filter(lambda x: x % 2 == 0, list(range(0, 100))))

print(numeros_pares)