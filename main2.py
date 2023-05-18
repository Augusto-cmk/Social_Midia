from src.repository.person_repository import PersonRepository
from src.repository.post_repository import PostRepository

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

