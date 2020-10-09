'''
    Compara o comprimento das strings passadas pelo usuário
'''
def comparaStrings():
    s1 = input("Digite o conteúdo da string 1: ")
    s2 = input("Digite o conteúdo da string 2: ")

    print("String 1: ", s1)
    print("String 2: ", s2)

    tam_s1 = len(s1)
    tam_s2 = len(s2)

    print("Tamanho da string 1: ", tam_s1, " caracteres")
    print("Tamanho da string 2: ", tam_s2, " caracteres")

    if tam_s1 == tam_s2:
        print("As duas strings possuem o mesmo tamanho")
    else:
        print("As duas strings possuem tamanhos diferentes")

comparaStrings()

