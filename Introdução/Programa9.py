'''
    Devolve o nome do usuário digitado de trás pra frente em caixa alta
'''
def nome():
    n = input("Digite seu nome aqui: ")
    print(n[::-1].upper())

nome()