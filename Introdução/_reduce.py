from functools import reduce
'''
    - Exemplo simples utilizando a função reduce com uma função lambda(anônima)
    - Onde é extraído o maior valor de uma lista
'''

lista = [100, 200, 300, 400, 500]

maior = reduce((lambda x, y: x if (x > y) else y), lista)

print(maior)