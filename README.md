# Descrição do Projeto

Breve explicação e os passos realizados no projeto.

## Passos Realizados

1. **Preparação do Ambiente**: Já possuía o MongoDB instalado em meu sistema, não precisei instalar novamente.

2. **Criação das Collections**: No banco de dados local do MongoDB, criei as collections "carros" e "montadoras".

3. **Desenvolvimento em Python**: No VSCode, criei um arquivo Python onde importei a biblioteca `pandas`. Em seguida, criei dois DataFrames que correspondiam as tabelas: "carros" e "montadoras", já com os dados inseridos.

4. **Conexão com o MongoDB**: Utilizando a biblioteca `pymongo`, fiz a conexão no MongoDB local. Salvei os dados (passo 3) nas collections (passo 2), convertendo os DataFrames em listas de dicionários, que é o formato utilizado pelo MongoDB.

5. **Relacionamento entre Collections**: Realizei um relacionamento (join) entre as duas collections. Fiz um loop que percorre cada carro, extraindo a montadora de cada um. Essa informação da montadora foi utilizada para acessar a collection de "montadoras" e obter dados adicionais, como o país de origem.

6. **Agregação de Dados**: No último passo, realizei uma agregação com base no campo "País". O operador `$group` foi utilizado para agrupar os dados pelo campo "País". Criei um array chamado "Carros" utilizando o operador `$push` para armazenar as informações dos carros relacionadas a cada país.


