'''
    Retorna o custo de um produto antes e após a aplicação do imposto passado
'''
def somaImposto(custo, taxa: float):
    print("Custo do item sem imposto: ", custo)
    custo += custo * (taxa / 100)
    print("Custo do item com imposto: ", custo)
somaImposto(60, 5)

