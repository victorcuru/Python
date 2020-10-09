'''
    Programa que retorna uma string na vertical com texto em cx alta
'''
nome = input("Digite seu nome aqui: ")
cont = 0

while(cont < len(nome)):
    c = cont
    print(nome[c].upper())
    cont += 1