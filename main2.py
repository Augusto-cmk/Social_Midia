from src.repository.person_repository import PersonRepository
from src.repository.post_repository import PostRepository
from src.repository.friend_repository import FriendRepository
from src.repository.comment_repository import CommentRepository
from src.repository.post_repository import Post
from src.repository.person_status_repository import PersonStatusRepository


# Criando uma nova pessoa
person_data1 = {
    'name': 'John Doe',
    'age': 21,
    'photo': 'john.jpg',
    'email': 'john@example.com',
    'password': 'password123',
    'state': 'California',
    'city': 'Los Angeles'
}

person_data2 = {
    'name': 'Gabriel Doe',
    'age': 25,
    'photo': 'john.jpg',
    'email': 'john@example.com',
    'password': 'password123',
    'state': 'California',
    'city': 'Los Angeles'
}
person = PersonRepository()
person.insert_person(person_data1)
person.insert_person(person_data2)
person.search_person_all()

# Criando uma nova amizade
friendship_data = {
    'person_id': 1,
    'friend_id': 2
}
friend = FriendRepository()
friend.create_friendship(1, 2)

print("printando amigos do 1:")
person.print_friends(1)

# Criando um novo status de pessoa
person_status_data = {
    'person_id': 1,
    'status_text': 'Feeling great today!'
}

status = PersonStatusRepository()
status.insert_person_status(person_status_data)

# Criando um novo post
post_data = {
    'person_id': 1,
    'text': 'Hello friends! Hope you\'re all doing well.',
    'image': 'post1.jpg'
}

post = PostRepository()
post.create_post(post_data)

post = person.get_person_posts(1)
for p in post:
    print(p.text, p.image)

# Criando um novo comentário em um post
comment_data = {
    'post_id': 1,
    'person_id': 2,
    'text': 'Glad to hear you\'re doing well!'
}

comment = CommentRepository()
comment.create_comment(1, 1, 'Glad to hear you\'re doing well!')

print(comment.show_comment(1))