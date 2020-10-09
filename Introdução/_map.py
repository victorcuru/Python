'''
    - Exemplo de função map usada para trazer apenas as contas com valores acima de 1000 a partir de
    um dicionário
'''
accounts = [{'name': 'User 1', 'value': 100}, {'name': 'User 2', 'value': 5000}, {'name': 'User 3', 'value': 600},
            {'name': 'User 4', 'value': 2000}, {'name': 'User 5', 'value': 9898}]

print(list(map(lambda x: x if (x['value'] > 1000) else 'vazio', accounts)))