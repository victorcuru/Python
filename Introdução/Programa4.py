'''
    Retorna uma sequência de valores
'''
def linhas(n):
    for i in range(n):
        i += 1
        print((str(i) + " ") * i)

linhas(10)