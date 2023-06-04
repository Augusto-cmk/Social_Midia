from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from src.models.person import Person
from src.models.post import Post

from src.connection.connection import Connection

Base = declarative_base()


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    text = Column(String(255))
    date = Column(DateTime)
    post_id = Column(Integer, ForeignKey(Post.id))
    person_id = Column(Integer, ForeignKey(Person.id))

    def __repr__(self) -> str:
        return '<Comment {}>'.format(self.id)

    def save(self) -> None:
        session = Connection().get_session()
        session.add(self)
        session.commit()

    def delete(self) -> None:
        session = Connection().get_session()
        session.delete(self)
        session.commit()
