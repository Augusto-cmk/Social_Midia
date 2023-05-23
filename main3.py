from src.services.person_status_service import PersonStatusService
from src.services.person_service import PersonService
from src.services.friend_service import FriendService
from src.services.post_service import PostService

person_data1 = {
    'name': 'John Doe',
    'birthday': "12/10/2021",
    'photo': 'john.jpg',
    'email': 'john@example.com',
    'password': 'password123',
    'state': 'California',
    'city': 'Los Angeles'
}


# person = PersonService()
# person.register_person(person_data1)
variavel = PersonService().get_person_all()
ids = [person['id'] for person in variavel]
print(ids)
# id = PersonService().id_person('john@example.com','password123')

person_status_data = {
    'profession': 'ga',
    'university': 'ufv',
    'course': 'hello',
    'web_site': 'ww.com',
    'linkedin': "kjhdajf",
}

FriendService.create_friendship(2, 1)
a = PersonService()
print(a.get_friends_person(2)[0]['name'])

