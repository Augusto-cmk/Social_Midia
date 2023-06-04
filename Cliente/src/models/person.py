from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from src.connection.connection import Connection

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), index=True)
    photo = Column(String)
    email = Column(String)
    password = Column(String)
    state = Column(String)
    city = Column(String)
    birthday = Column(String)

    def __repr__(self) -> str:
        return '<Person {}>'.format(self.name)

    def save(self) -> None:
        session = Connection().get_session()
        session.add(self)
        session.commit()

    def delete(self) -> None:
        session = Connection().get_session()
        session.delete(self)
        session.commit()
