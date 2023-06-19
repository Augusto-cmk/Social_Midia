import sqlite3


class Connection:
    def __init__(self) -> None:
        self.__connection = None
        self.connect()

    def connect(self) -> None:
        self.__connection = sqlite3.connect('braincase.db')
        self.create_tables()

    def get_connection(self) -> sqlite3.Connection:
        return self.__connection

    def create_tables(self) -> None:
        with self.__connection:
            cursor = self.__connection.cursor()

            # Criação da tabela person
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS person (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(40),
                    photo VARCHAR,
                    email VARCHAR,
                    password VARCHAR,
                    state VARCHAR,
                    birthday VARCHAR,
                    city VARCHAR
                )
            """)

            # Criação da tabela friend
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS friend (
                    id INTEGER PRIMARY KEY,
                    person_id INTEGER,
                    friend_id INTEGER,
                    FOREIGN KEY (person_id) REFERENCES person (id),
                    FOREIGN KEY (friend_id) REFERENCES person (id)
                )
            """)

            # Criação da tabela person_status
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS person_status (
                    id INTEGER PRIMARY KEY,
                    person_id INTEGER,
                    profession VARCHAR(50),
                    university VARCHAR(50),
                    course VARCHAR(50),
                    web_site VARCHAR,
                    linkedin VARCHAR,
                    FOREIGN KEY (person_id) REFERENCES person (id)
                )
            """)

            # Criação da tabela comment
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS comment (
                    id INTEGER PRIMARY KEY,
                    text VARCHAR(255),
                    date DATETIME,
                    post_id INTEGER,
                    person_id INTEGER,
                    FOREIGN KEY (post_id) REFERENCES post (id),
                    FOREIGN KEY (person_id) REFERENCES person (id)
                )
            """)

            # Criação da tabela post
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS post (
                    id INTEGER PRIMARY KEY,
                    text VARCHAR(255),
                    image VARCHAR,
                    curtir INTEGER,
                    date DATETIME,
                    author_id INTEGER,
                    FOREIGN KEY (author_id) REFERENCES person (id)
                )
            """)

            # Criação da tabela message
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS message(
                    id INTEGER PRIMARY KEY,
                    text VARCHAR(255),
                    date DATETIME,
                    author_id INTEGER,
                    destine_id INTEGER,
                    FOREIGN KEY (author_id) REFERENCES person (id),
                    FOREIGN KEY (destine_id) REFERENCES person (id)
                )
            """)
