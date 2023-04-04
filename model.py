from pymongo import MongoClient
from bson.objectid import ObjectId

class PersonModel:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def create_person(self, name: str, age: int) -> str:
        try:
            result = self.collection.insert_one({"name": name, "age": age})
            person_id = str(result.inserted_id)
            print(f"Person {name} created with id: {person_id}")
            return person_id
        except Exception as error:
            print(f"An error occurred while creating person: {error}")
            return None

    def read_person_by_id(self, person_id: str) -> dict:
        try:
            person = self.collection.find_one({"_id": ObjectId(person_id)})
            if person:
                print(f"Person found: {person}")
                return person
            else:
                print(f"No person found with id {person_id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading person: {error}")
            return None

    def update_person(self, person_id: str, name: str, age: int) -> int:
        try:
            result = self.collection.update_one({"_id": ObjectId(person_id)}, {"$set": {"name": name, "age": age}})
            if result.modified_count:
                print(f"Person {person_id} updated with name {name} and age {age}")
            else:
                print(f"No person found with id {person_id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating person: {error}")
            return None

    def delete_person(self, person_id: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(person_id)})
            if result.deleted_count:
                print(f"Person {person_id} deleted")
            else:
                print(f"No person found with id {person_id}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting person: {error}")
            return None

class BookModel:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def create_book(self, _id: int, titulo: str, autor: str, ano: int, preco: float) -> str:
        try:
            result = self.collection.insert_one({"_id": _id, "titulo": titulo, "autor": autor, "ano": ano, "preco": preco})
            book_id = str(result.inserted_id)
            print(f"Person {titulo} created with id: {book_id}")
            return book_id
        except Exception as error:
            print(f"An error occurred while creating book: {error}")
            return None

    def read_book_by_id(self, book_id: str) -> dict:
        try:
            book = self.collection.find_one({"_id": ObjectId(book_id)})
            if book:
                print(f"Book found: {book}")
                return book
            else:
                print(f"No book found with id {book_id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading book: {error}")
            return None

    def update_book(self, book_id: str, _id: int, titulo: str, autor: str, ano: int, preco: float) -> int:
        try:
            result = self.collection.update_one({"_id": ObjectId(book_id)}, {"$set": {"_id": _id, "titulo": titulo, "autor": autor, "ano": ano, "preco": preco}})
            if result.modified_count:
                print(f"Book {book_id} updated with title {titulo} published in {ano} , by {autor} costing {preco}")
            else:
                print(f"No book found with id {book_id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating book: {error}")
            return None

    def delete_book(self, book_id: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(book_id)})
            if result.deleted_count:
                print(f"Book {book_id} deleted")
            else:
                print(f"No book found with id {book_id}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting book: {error}")
            return None