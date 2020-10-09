'''
    Compara os valores dos produtos passados
'''
p1 = float(input("Qual o preço do produto 1? "))
p2 = float(input("Qual o preço do produto 2? "))
p3 = float(input("Qual o preço do produto 3? "))

if p1 < p2 and p1 < p3:
    print("O produto 1 é o mais barato")
if p2 < p1 and p2 < p3:
    print("O produto 2 é o mais barato")
if p3 < p1 and p3 < p2:
    print("O produto 3 é o mais barato")