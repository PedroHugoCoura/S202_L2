from database import Database
from DAO.ZoologicoDAO import ZoologicoDAO

db = Database(database="Zoologico", collection="Animais")
db.resetDatabase()

zoo = ZoologicoDAO(db)


