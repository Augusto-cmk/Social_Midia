from src.repository.person_repository import PersonRepository
from src.repository.post_repository import PostRepository
from src.repository.friend_repository import FriendRepository
from src.repository.comment_repository import CommentRepository
from src.repository.post_repository import Post
from src.services.person_status_service import PersonStatusService


# Criando uma nova pessoa
person_data1 = {
    'name': 'John Doe',
    'birthday': "12/10/2021",
    'photo': 'john.jpg',
    'email': 'john@example.com',
    'password': 'password123',
    'state': 'California',
    'city': 'Los Angeles'
}


person = PersonRepository()
person.insert_person(person_data1)
# print(person.get_person_all())
id = person._get_person_id('john@example.com','password123')
print(person.get_person(id))
