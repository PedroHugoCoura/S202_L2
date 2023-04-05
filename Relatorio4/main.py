from database import Database
from save_json import writeAJson

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()

class ProductAnalyzer:
    def __init__(self, db):
        self.db = db

    def questaoUm(self):
        result = self.db.collection.aggregate([
            {"$match": {"cliente_id": "B"}},
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id",
                        "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}
        ])
        writeAJson(result, "questaoUm")

    def questaoDois(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "quantidade": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"quantidade": -1}},
            {"$limit": 1}
        ])
        writeAJson(result, "questaoDois")

    def questaoTres(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id",
                        "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": 1}},
            {"$limit": 1}
        ])
        writeAJson(result, "questaoTres")

    def questaoQuatro(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "quantidade": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"quantidade": {"$gt": 2}}}
        ])
        writeAJson(result, "questaoQuatro")

analyzer = ProductAnalyzer(db)

analyzer.questaoUm()
analyzer.questaoDois()
analyzer.questaoTres()
analyzer.questaoQuatro()



