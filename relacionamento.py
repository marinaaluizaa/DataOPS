from pymongo import MongoClient
import pandas as pd

#conecta no banco
client = MongoClient('mongodb://localhost:27017/')  
db = client['local'] 

# dados das collection
carros_collection = db['Carros']

# une as collection e extrai País
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
    },
    {
        '$project': {
            '_id': 0,  
            'Carro': 1,  
            'Cor': 1,  
            'Montadora': 1, 
            'País': '$montadora_info.País' 
        }
    }
]

# executa a agregacao
relacionamento = carros_collection.aggregate(pipeline)

# exibe a formatacao da agregacao em tabela
table = pd.DataFrame(list(relacionamento))
print(table)
