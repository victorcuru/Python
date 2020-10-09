'''
    Função que retorna o aumento de salário reajustado
'''
def aumento_salario(salario):

    print("Salário atual: ", salario)

    if salario <= 280:
        salario += salario * 0.20
        print("O salário teve um reajuste de 20 %. Seu valor atual é de: ", salario, " reais")
    elif 280 < salario <= 700:
        salario += salario * 0.15
        print("O salário teve um reajuste de 15%. Seu valor atual é de: ", salario, " reais")
    elif 700 < salario <= 1500:
        salario += salario * 0.10
        print("O salário teve um reajuste de 10%. Seu valor atual é de: ", salario, " reais")
    elif salario > 1500:
        salario += salario * 0.05
        print("O salário teve um reajuste de 5%. Seu valor atual é de: ", salario, " reais")
    else:
        ("Aumento não definido!")

aumento_salario(2000)



