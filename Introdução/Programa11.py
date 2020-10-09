'''
    Programa que retorna a data de nascimento com o mês escrito por extenso
'''

def data_extenso():
    data_nasc = input("Digite a data de nascimento: ")
    mes_ext = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio',
               6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro',
               11: 'Novembro', 12: 'Dezembro'}
    try:
        dia, mes, ano = data_nasc.split("/")
        print("Data de nascimento: %s/%s/%s" % (dia, mes_ext[int(mes)], ano))
    except ValueError:
        print("Por favor utilize o formato específico 'dd/mm/aaaa' para uma data válida")

data_extenso()

