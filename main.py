from database import Database
from save_json import writeAJson
from model import PersonModel
from model import BookModel

db = Database(database="relatorio5", collection="pessoas")
db.resetDatabase()
# person_model = PersonModel(db)
#
# # cria nova entradapessoa
# id_pessoa = person_model.create_person("João Silva", 30)
#
# # le pelo id
# pessoa = person_model.read_person_by_id(id_pessoa)
#
# # att
# person_model.update_person(id_pessoa, "Maria Silva", 35)

# AGORA PARA OS LIVROS
book_model = BookModel(db)

# cria nova entradapessoa
id_book = book_model.create_book(1, "Ação Humana", "Ludwig Von Mises", 1940, 50.00)

# le pelo id
book = book_model.read_book_by_id(id_book)

# att
book_model.update_book(id_book,1,"Seis Lições","Ludwig Von Mises",1979, 40.00)

#delete
book_model.delete_book(id_book)
