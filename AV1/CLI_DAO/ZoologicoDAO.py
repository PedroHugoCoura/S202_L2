from pymongo import MongoClient
from bson.objectid import ObjectId


class ZooDAO:
    def __init__(self, db):
        self.collection = db.animals

    def createAnimal(self, animal):
        try:
            animal_dict = {"id": animal.id,
                           "nome": animal.nome,
                           "especie": animal.especie,
                           "idade": animal.idade,
                           "habitat": animal.habitat}
            resultado = self.collection.insert_one(animal_dict)
            id_animal = str(resultado.inserted_id)
            print(f"Animal {animal.nome} criado com id: {animal.id}")
            return id_animal
        except Exception as erro:
            print(f"Erro ao criar um animal: {erro}")
            return None

    def readAnimal(self, id_animal):
        try:
            animal = self.collection.find_one({"_id": ObjectId(id_animal)})
            if animal:
                print(f"Animal encontrado: {animal}")
                return animal
            else:
                print(f"Nenhum animal encontrado com id {id_animal}")
                return None
        except Exception as erro:
            print(f"Erro ao ler um animal: {erro}")
            return None

    def updateAnimal(self, id_animal, animal):
        try:
            animal_dict = {"id": animal.id,
                           "nome": animal.nome,
                           "especie": animal.especie,
                           "idade": animal.idade,
                           "habitat": animal.habitat}
            resultado = self.collection.update_one({"_id": ObjectId(id_animal)}, {"$set": animal_dict})
            if resultado.modified_count:
                print(f"Animal {id_animal} atualizado com nome {animal.nome}, espécie {animal.especie}, idade {animal.idade} e habitat {animal.habitat}")
            else:
                print(f"Nenhum animal encontrado com id {id_animal}")
            return resultado.modified_count
        except Exception as erro:
            print(f"Erro ao atualizar um animal: {erro}")
            return None

    def deleteAnimal(self, id_animal):
        try:
            resultado = self.collection.delete_one({"_id": ObjectId(id_animal)})
            if resultado.deleted_count:
                print(f"Animal {id_animal} deletado")
            else:
                print(f"Nenhum animal encontrado com id {id_animal}")
            return resultado.deleted_count
        except Exception as erro:
            print(f"Erro ao deletar um animal: {erro}")
            return None
