from DAO.ZoologicoDAO import ZoologicoDAO
from model.Habitat import Habitat
from model.Cuidador import Cuidador
from model.Animal import Animal

class ZoologioCLI:

    def __init__(self):
        pass

    def menu(self):
        op = input("Escreva a opção que deseja: [1]Criar\n [2]Pesquisar\n [3]Atualizar\n [4]Deletar:")
        if op == 1:
            print("O animal foi criado com o id: ", ZoologioCLI.createAnimal(self))
        elif op == 2:
            ZoologioCLI.readAnimal(self)
        elif op == 3:
            ZoologioCLI.updateAnimal(self)
        elif op == 4:
            ZoologioCLI.deleteAnimal(self)


    def createAnimal(self):

        #cuidador
        id_Cuidador = input("Insira o id do cuidador: ")
        nome_Cuidador = input("Insira o nome do cuidador: ")
        documento_Cuidador = input("Insira o documento do cuidador: ")
        cuidador = Cuidador(id_Cuidador, nome_Cuidador, documento_Cuidador)

        #habitat
        id_Habitat = input("Insira o id do habitat: ")
        nome_Habitat = input("Insira o nome do habitat: ")
        tipo_AmbienteHabitat = input("Tipo do ambiente do habitat: ")
        habitat = Habitat(id_Habitat, nome_Habitat, tipo_AmbienteHabitat, cuidador)

        #animal
        id_Animal = input("Insira o id do animal: ")
        nome_Animal = input("Insira o nome do animal: ")
        especie_Animal = input("Insira a especie do animal: ")
        idade_Animal = input("Insira a idade do animal: ")
        animal = Animal(id_Animal, nome_Animal, especie_Animal, idade_Animal, habitat)

        idAnimalCriado = ZoologicoDAO.create_animal(animal)
        return idAnimalCriado

    def readAnimal(self):
        id = input("Insira o id do animal a ser pesquisado:")
        ZoologicoDAO.read_animal_by_id(id)

    def updateAnimal(self):
        id = input("Insira o id do animal a ser atualizado:")
        print("Agora digite as informações a serem atualizadas")

        #cuidador
        id_Cuidador = input("Insira o id do cuidador: ")
        nome_Cuidador = input("Insira o nome do cuidador: ")
        documento_Cuidador = input("Insira o documento do cuidador: ")
        cuidador = Cuidador(id_Cuidador, nome_Cuidador, documento_Cuidador)

        #habitat
        id_Habitat = input("Insira o id do habitat: ")
        nome_Habitat = input("Insira o nome do habitat: ")
        tipo_AmbienteHabitat = input("Tipo do ambiente do habitat: ")
        habitat = Habitat(id_Habitat, nome_Habitat, tipo_AmbienteHabitat, cuidador)

        #animal
        id_Animal = input("Insira o id do animal: ")
        nome_Animal = input("Insira o nome do animal: ")
        especie_Animal = input("Insira a especie do animal: ")
        idade_Animal = input("Insira a idade do animal: ")
        animal = Animal(id_Animal, nome_Animal, especie_Animal, idade_Animal, habitat)

        ZoologicoDAO.update_animal(id, animal)

    def deleteAnimal(self):
        id = input("Insira o id do animal a ser deletado:")
        ZoologicoDAO.delete_animal(id)
