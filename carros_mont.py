import pandas as pd

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

# Exibe os dados dos carros em formato de DataFrame
print("Carros:")
print(data_carros)

# Exibe os dados das montadoras em formato de DataFrame
print("\nMontadora:")
print(data_montadora)
