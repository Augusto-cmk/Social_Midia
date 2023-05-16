from src.connection.connection import Connection
from src.models.person import Person


class PersonRepository:
    def __init__(self):
        self.__session = Connection().get_session()

    def insert_person(self, data_person: dict) -> None:
        person = Person(name=data_person.get('name'),
                        age=data_person.get('age'),
                        photo=data_person.get('photo'),
                        email=data_person.get('email'),
                        password=data_person.get('password'),
                        state=data_person.get('state'),
                        city=data_person.get('city'))
        person.save()

    def search_person_all(self) -> None:
        persons = self.__session.query(Person).all()
        for person in persons:
            print(f"ID: {person.id}, Nome: {person.name}, Idade: {person.age}")

    def get_person_id(self) -> int:
        result = self.__session.query(Person.id).filter(Person.name == "Jao").first()
        if result:
            person_id = result.id
            return person_id
