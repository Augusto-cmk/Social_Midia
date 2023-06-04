from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from src.models.person import Person

from src.connection.connection import Connection

Base = declarative_base()


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    text = Column(String(40), index=True)
    image = Column(String)
    curtir = Column(Integer)
    date = Column(DateTime)
    author_id = Column(Integer, ForeignKey(Person.id))

    def __repr__(self) -> str:
        return '<Post {}>'.format(self.id)

    def save(self) -> None:
        session = Connection().get_session()
        session.add(self)
        session.commit()

    def delete(self) -> None:
        session = Connection().get_session()
        session.delete(self)
        session.commit()
