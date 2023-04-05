# https://github.com/PedroHugoCoura/S202_L2 -------------> Link GitHub

class Animal:
    def __init__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som
    
    def emitir_som(self):
        print(self.som)
    
    def mudar_cor(self, nova_cor):
        self.cor = nova_cor

class Elefante(Animal):
    def __init__(self, nome, idade, especie, cor, som, tamanho):
        super().__init__(nome, idade, especie, cor, som)
        self.tamanho = tamanho
    
    def trombar(self):
        print("Paaah")
    
    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho

elefante = Elefante(input("Digite o nome do elefante: "), int(input("Digite a idade do elefante: ")), input("Digite a espécie do elefante: "), input("Digite a cor do elefante: "), "", input("Digite o tamanho do elefante: "))

if elefante.especie == "Africano" and elefante.idade < 10:
    elefante.mudar_tamanho("pequeno")
    elefante.som = "Paaah"
elif elefante.especie == "Africano" and elefante.idade >= 10:
    elefante.mudar_tamanho("grande")
    elefante.som = "PAHHHHHH"

elefante.emitir_som()
elefante.mudar_cor("cinza")
print("Novo tamanho:", elefante.tamanho)
print("Novo som:", elefante.som)
