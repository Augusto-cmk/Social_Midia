from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from src.models.person import Person

from src.connection.connection import Connection

Base = declarative_base()


class Friend(Base):
    __tablename__ = 'friend'

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey(Person.id))
    friend_id = Column(Integer, ForeignKey(Person.id))

    def __repr__(self) -> str:
        return '<Friend {}>'.format(self.id)

    def save(self) -> None:
        session = Connection().get_session()
        session.add(self)
        session.commit()

    def delete(self) -> None:
        session = Connection().get_session()
        session.delete(self)
        session.commit()
