from pymongo import MongoClient
from CRUD import BookModel


client = MongoClient("mongodb://localhost:27017/")
db = client["Livros"]
book_model = BookModel(db)

book_id = book_model.create_book("1984", "George Orwell", 1949, 20.5)

book_model.read_book_by_id(book_id)

book_model.update_book(book_id,"Moby Dick", "Herman  Melville", 1851, 29.9)

book_model.read_book_by_id(book_id)

book_model.delete_book('642c975c5271248b6bb63e32')


