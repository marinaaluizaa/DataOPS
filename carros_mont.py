import pandas as pd
from pymongo import MongoClient

# Dados dos carros
dados_carros = {
    'Carro': ['Onix', 'Polo', 'Sandero', 'Fiesta', 'City'],
    'Cor': ['Prata', 'Branco', 'Prata', 'Vermelho', 'Preto'],
    'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda']
}

data_carros = pd.DataFrame(dados_carros)

# Dados das montadoras
dados_montadora = {
    'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda'],
    'País': ['EUA', 'Alemanha', 'França', 'EUA', 'Japão']
}

data_montadora = pd.DataFrame(dados_montadora)

# dados dos carros
# print("Carros:")
# print(data_carros)

# dados das montadoras 
# print("\nMontadora:")
# print(data_montadora)

client = MongoClient('mongodb://localhost:27017/')  # URI padrão do MongoDB local
db = client['local'] 

carros_dict = data_carros.to_dict('records')
montadoras_dict = data_montadora.to_dict('records')

# insere os dados na collection carros
carros_collection = db['Carros']
carros_collection.insert_many(carros_dict)

# insere os dados na collection montadoras
montadoras_collection = db['Montadoras']
montadoras_collection.insert_many(montadoras_dict)