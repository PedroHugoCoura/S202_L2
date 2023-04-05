import pymongo
import json

# Conectar ao banco de dados
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pokedex"]
collection = db["pokedex"]

# Função para pesquisar pokémons pelo ID
def search_by_id(id):
    result = collection.find_one({"id": id})
    with open(f"id_{id}.json", "w") as file:
        json.dump(result, file)
    print(f"Resultado da pesquisa salvo em id_{id}.json")

# Função para pesquisar pokémons pelo nome
def search_by_name(name):
    result = collection.find_one({"name": name})
    with open(f"name_{name}.json", "w") as file:
        json.dump(result, file)
    print(f"Resultado da pesquisa salvo em name_{name}.json")

# Função para pesquisar pokémons pelo tipo
def search_by_type(type):
    result = collection.find({"type": type})
    with open(f"type_{type}.json", "w") as file:
        for pokemon in result:
            json.dump(pokemon, file)
    print(f"Resultado da pesquisa salvo em type_{type}.json")

# Função para pesquisar pokémons com base em suas estatísticas
def search_by_base(stat, value):
    result = collection.find({f"base.{stat}": {"$gte": value}})
    with open(f"base_{stat}_{value}.json", "w") as file:
        for pokemon in result:
            json.dump(pokemon, file)
    print(f"Resultado da pesquisa salvo em base_{stat}_{value}.json")

# Função para pesquisar pokémons com base em suas habilidades
def search_by_ability(ability):
    result = collection.find({"abilities": ability})
    with open(f"ability_{ability}.json", "w") as file:
        for pokemon in result:
            json.dump(pokemon, file)
    print(f"Resultado da pesquisa salvo em ability_{ability}.json")
