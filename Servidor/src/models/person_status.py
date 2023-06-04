from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from src.models.person import Person

from src.connection.connection import Connection

Base = declarative_base()


class PersonStatus(Base):
    __tablename__ = 'person_status'

    id = Column(Integer, primary_key=True)
    profession = Column(String(50))
    university = Column(String(50))
    course = Column(String(50))
    web_site = Column(String)
    linkedin = Column(String)
    person_id = Column(Integer, ForeignKey(Person.id))

    def __repr__(self) -> str:
        return '<PersonStatus {}>'.format(self.id)

    def save(self) -> None:
        session = Connection().get_session()
        session.add(self)
        session.commit()

    def delete(self) -> None:
        session = Connection().get_session()
        session.delete(self)
        session.commit()
