from src.connection.connection import Connection

import json


class PostRepository:
    def __init__(self):
        self.__connection = Connection().get_connection()

    def _create_post(self, data_post: dict) -> int:
        try:
            cursor = self.__connection.cursor()
            cursor.execute(
                "INSERT INTO post (text, image, curtir, date, author_id) VALUES (?, ?, ?, ?, ?)",
                (data_post['text'], data_post['image'], data_post['curtir'], data_post['date'], data_post['author_id'])
            )
            self.__connection.commit()
            return True
        except Exception:
            return False

    def add_like(self, id_post):
        try:
            cursor = self.__connection.cursor()
            cursor.execute("UPDATE post SET curtir = curtir + 1 WHERE id = ?", (id_post,))
            self.__connection.commit()
        except Exception:
            pass

    def get_posts_user(self, author_id) -> list:
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM post WHERE author_id = ? ORDER BY date", (author_id,))
        result = cursor.fetchall()
        posts_user = [
            {
                "id": row[0],
                "text": row[1],
                "image": row[2],
                "curtir": row[3],
                "date": row[4],
                "author_id": row[5]
            } for row in result
        ]
        return posts_user

    def get_posts_all(self):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM post")
        result = cursor.fetchall()
        for row in result:
            print(row[1])

    def get_post_comments(self, post_id: int):
        cursor = self.__connection.cursor()
        cursor.execute(
            "SELECT c.id, c.text, c.post_id, c.person_id, c.date "
            "FROM comment AS c "
            "WHERE c.post_id = ? "
            "ORDER BY c.date",
            (post_id,)
        )
        result = cursor.fetchall()
        comments_data = [
            {
                'id': row[0],
                'text': row[1],
                'post_id': row[2],
                'person_id': row[3],
                'date': row[4].strftime('%Y-%m-%d %H:%M:%S')
            } for row in result
        ]
        return json.dumps(comments_data)

    def get_ordered_comments(self, post_id: int):
        cursor = self.__connection.cursor()
        cursor.execute(
            "SELECT * FROM comment WHERE post_id = ? ORDER BY date ASC",
            (post_id,)
        )
        result = cursor.fetchall()
        comments_list = [
            {
                'id': row[0],
                'text': row[1],
                'date': row[2],
                'author_id': row[4],
                'post_id': row[3]
            } for row in result
        ]
        return comments_list

    def remove_post(self,id_post):
        cursor = self.__connection.cursor()
        try:
            cursor.execute(
                "DELETE FROM post WHERE id = ?", (id_post,)
            )
            self.__connection.commit()
            return True
        except Exception:
            return False