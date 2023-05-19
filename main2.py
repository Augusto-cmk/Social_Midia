from src.repository.person_repository import PersonRepository
from src.repository.post_repository import PostRepository
from src.repository.friend_repository import FriendRepository
from src.repository.comment_repository import CommentRepository
from src.repository.post_repository import Post
from src.repository.person_status_repository import PersonStatusRepository

# Cria uma instância do PersonRepository
person_repo = PersonRepository()

# Dicionário com dados de uma pessoa
person_data = {
    "name": "Jao",
    "age": 23,
    "photo": "photo.jpg",
    "email": "gabriel@example.com",
    "password": "123456",
    "state": "MG",
    "city": "Florestal",
    "birthday": "12/10/2021"
}

# Insere uma pessoa no banco de dados
person_repo.insert_person(person_data)

# Lista todas as pessoas no banco de dados
person_repo.search_person_all()

# Obtém o ID de uma pessoa pelo nome
person_id = person_repo.get_person_id()
print(f"Person ID: {person_id}")

# Cria uma instância do PostRepository
post_repo = PostRepository()

# Dicionário com dados de um post
post_data = {
    "text": "Hello World!",
    "image": "image.jpg",
    "person_id": person_id
}

# Cria um post no banco de dados
post_repo.create_post(post_data)

# Lista todos os posts no banco de dados
post_repo.search_post_all()

# Criando uma nova pessoa
person_data1 = {
    'name': 'John Doe',
    'age': 25,
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

# Criando uma nova amizade
friendship_data = {
    'person_id': 1,
    'friend_id': 2
}
friend = FriendRepository()
friend.create_friendship(1, 2)

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

# Criando um novo comentário em um post
comment_data = {
    'post_id': 1,
    'person_id': 2,
    'text': 'Glad to hear you\'re doing well!'
}

comment = CommentRepository()
comment.create_comment(1, 2, 'Glad to hear you\'re doing well!')
