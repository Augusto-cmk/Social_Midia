from typing import Any

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker, Session


class Connection:
    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///braincase.db')
        self.db_session = scoped_session(sessionmaker(autocommit=False, bind=self.engine))
        self.create_tables()

    def get_session(self) -> scoped_session[Session | Any]:
        return self.db_session

    def create_tables(self) -> None:
        with self.engine.connect() as connection:
            statement = text(
                """
                CREATE TABLE IF NOT EXISTS person (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(40),
                    age INTEGER,
                    photo VARCHAR,
                    email VARCHAR,
                    password VARCHAR,
                    state VARCHAR,
                    city VARCHAR
                )
                """
            )
            connection.execute(statement)

            statement = text(
                """
                CREATE TABLE IF NOT EXISTS friend (
                    id INTEGER PRIMARY KEY,
                    person_id INTEGER,
                    friend_id INTEGER,
                    FOREIGN KEY (person_id) REFERENCES person (id),
                    FOREIGN KEY (friend_id) REFERENCES person (id)
                )
                """
            )
            connection.execute(statement)

            statement = text(
                """
                CREATE TABLE IF NOT EXISTS person_status (
                    id INTEGER PRIMARY KEY,
                    person_id INTEGER,
                    status_text VARCHAR(255),
                    profession VARCHAR(50),
                    university VARCHAR(50),
                    course VARCHAR(50),
                    web_site VARCHAR,
                    linkedin VARCHAR,
                    FOREIGN KEY (person_id) REFERENCES person (id)
                )
                """
            )
            connection.execute(statement)

            statement = text(
                """
                CREATE TABLE IF NOT EXISTS comment (
                    id INTEGER PRIMARY KEY,
                    text VARCHAR(255),
                    date DATETIME,
                    post_id INTEGER,
                    person_id INTEGER,
                    FOREIGN KEY (post_id) REFERENCES post (id),
                    FOREIGN KEY (person_id) REFERENCES person (id)
                )
                """
            )
            connection.execute(statement)

            statement = text(
                """
                CREATE TABLE IF NOT EXISTS post (
                    id INTEGER PRIMARY KEY,
                    text VARCHAR(255),
                    image VARCHAR,
                    curtir INTEGER,
                    date DATETIME,
                    author_id INTEGER,
                    FOREIGN KEY (author_id) REFERENCES person (id)
                )
                """
            )
            connection.execute(statement)
