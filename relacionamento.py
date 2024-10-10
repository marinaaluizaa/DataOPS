from pymongo import MongoClient

# conecta no banco
client = MongoClient('mongodb://localhost:27017/')  
db = client['local']  

# pega as informações das collection
carros_collection = db['Carros']
montadoras_collection = db['Montadoras']

# agregação com join
pipeline = [
    {
        '$lookup': {
            'from': 'Montadoras',  
            'localField': 'Montadora',  
            'foreignField': 'Montadora',  
            'as': 'montadora_info'  
        }
    },
    {
        '$unwind': '$montadora_info'  
    }
]

# executa a agregacao criada
agregacao = carros_collection.aggregate(pipeline)

# exibe o resultado da agregacao
for resultado in agregacao:
    print({
        'Carro': resultado['Carro'],
        'Cor': resultado['Cor'],
        'Montadora': resultado['Montadora'],
        'País da Montadora': resultado['montadora_info']['País']
    })

print("relacionamento feito")
