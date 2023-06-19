from src.connection.connection import Connection
from src.models.person import Person
from src.models.post import Post
from src.models.friend import Friend
from src.models.comment import Comment

import json


class PersonRepository:
    def __init__(self):
        self.__connection = Connection().get_connection()

    @staticmethod
    def insert_person(data_person: dict) -> None:
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO person (name, photo, email, password, state, city, birthday) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (data_person['name'], data_person['photo'], data_person['email'], data_person['password'],
                 data_person['state'], data_person['city'], data_person['birthday'])
            )
            connection.commit()
        except Exception:
            pass

    def refresh_profile(self, id_person, data_person: dict) -> bool:
        try:
            cursor = self.__connection.cursor()
            cursor.execute(
                "UPDATE person SET birthday = ?, city = ?, email = ?, name = ?, password = ?, photo = ?, state = ? WHERE id = ?",
                (data_person['birthday'], data_person['city'], data_person['email'], data_person['name'],
                 data_person['password'], data_person['photo'], data_person['state'], id_person)
            )
            self.__connection.commit()
            return True
        except Exception:
            return False

    def get_person_all(self) -> list:
        cursor = self.__connection.cursor()
        cursor.execute("SELECT id, name FROM person")
        result = cursor.fetchall()
        list_persons = [
            {'id': row[0], 'name': row[1]} for row in result
        ]
        return list_persons

    def _get_person_password(self, email: str) -> str:
        cursor = self.__connection.cursor()
        cursor.execute("SELECT password FROM person WHERE email = ?", (email,))
        result = cursor.fetchone()
        if result:
            return result[0]
        return None

    def _get_person_id(self, email: str, password: str) -> int:
        cursor = self.__connection.cursor()
        cursor.execute("SELECT id FROM person WHERE email = ? AND password = ?", (email, password))
        result = cursor.fetchone()
        if result:
            return result[0]
        return None

    def get_person_1(self, person_id):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM person WHERE id = ?", (person_id,))
        result = cursor.fetchone()
        if result:
            person = {
                "id": result[0],
                "name": result[1],
                "photo": result[2],
                "email": result[3],
                "password": result[4],
                "state": result[5],
                "city": result[6],
                "birthday": result[7]
            }
            return person
        return None

    def get_friends_posts(self, person_id: int) -> str:
        cursor = self.__connection.cursor()
        cursor.execute(
            "SELECT p.id, p.text, p.image, p.likes, p.date, p.author_id "
            "FROM post AS p "
            "JOIN friend AS f ON p.author_id = f.friend_id "
            "WHERE f.person_id = ? "
            "ORDER BY p.date DESC",
            (person_id,)
        )
        result = cursor.fetchall()
        posts_data = []
        for row in result:
            post_data = {
                'id': row[0],
                'text': row[1],
                'image': row[2],
                'likes': row[3],
                'date': row[4].strftime('%Y-%m-%d %H:%M:%S'),
                'author_id': row[5]
            }
            posts_data.append(post_data)
        return json.dumps(posts_data)

    def like_friend_post(self, person_id: int, post_id: int) -> bool:
        try:
            cursor = self.__connection.cursor()
            cursor.execute("UPDATE post SET likes = likes + 1 WHERE id = ?", (post_id,))
            self.__connection.commit()
            return True
        except Exception:
            return False

    def comment_friend_post(self, person_id: int, post_id: int, text: str) -> bool:
        try:
            cursor = self.__connection.cursor()
            cursor.execute(
                "INSERT INTO comment (person_id, post_id, text) VALUES (?, ?, ?)",
                (person_id, post_id, text)
            )
            self.__connection.commit()
            return True
        except Exception:
            return False

    def get_friends(self, person_id: int):
        cursor = self.__connection.cursor()
        cursor.execute(
            "SELECT p.* "
            "FROM person AS p "
            "JOIN friend AS f ON p.id = f.friend_id "
            "WHERE f.person_id = ?",
            (person_id,)
        )
        result = cursor.fetchall()
        person_friends = [
            {
                "id": row[0],
                "name": row[1],
                "photo": row[2],
                "email": row[3],
                "password": row[4],
                "state": row[5],
                "city": row[6],
                "birthday": row[7]
            } for row in result
        ]
        return person_friends

    def get_person_posts(self, person_id: int) -> list:
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM post WHERE author_id = ?", (person_id,))
        result = cursor.fetchall()
        list_posts = [
            {
                "id": row[0],
                "text": row[1],
                "image": row[2],
                "likes": row[3],
                "date": row[4].strftime('%Y-%m-%d %H:%M:%S'),
                "author_id": row[5]
            } for row in result
        ]
        return list_posts

    def get_friends_count(self, person_id: int) -> int:
        cursor = self.__connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM friend WHERE person_id = ?", (person_id,))
        result = cursor.fetchone()
        if result:
            return result[0]
        return 0

    def get_colaboradores_count(self, person_id: int) -> int:
        cursor = self.__connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM friend WHERE friend_id = ?", (person_id,))
        result = cursor.fetchone()
        if result:
            return result[0]
        return 0
