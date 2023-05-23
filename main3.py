from src.services.person_status_service import PersonStatusService
from src.services.person_service import PersonService


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
print(PersonService().get_person_all())
# id = PersonService().id_person('john@example.com','password123')

person_status_data = {
    'profession': 'ga',
    'university': 'ufv',
    'course': 'hello',
    'web_site': 'ww.com',
    'linkedin': "kjhdajf",
}

# print(id)

# status = PersonStatusService()
# status.create_status_person(id,person_status_data)
# print(status.get_status_person(id))

# person_status_data = {
#     'Profession': 'ga',
#     'university': 'ufv',
#     'course': 'cc',
#     'web_site': 'ww.com',
#     'linkedin': "kjhdajf",
# }

# status = PersonStatusRepository()
# status._insert_person_status(person_status_data, 1)
# print(status.get_status_person(1))