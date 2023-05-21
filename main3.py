from src.repository.person_status_repository import PersonStatusRepository

person_status_data = {
    'status_text': 'Feeling great today!',
    'Profession': 'ga',
    'university': 'ufv',
    'course': 'cc',
    'web_site': 'ww.com',
    'linkedin': "kjhdajf",
}

status = PersonStatusRepository()
status.insert_person_status(person_status_data, 1)
print(status.get_status_person(1))

person_status_data = {
    'status_text': 'Feeling great today!',
    'Profession': 'ga',
    'university': 'ufv',
    'course': 'cc',
    'web_site': 'ww.com',
    'linkedin': "kjhdajf",
}

status = PersonStatusRepository()
status.insert_person_status(person_status_data, 1)
print(status.get_status_person(1))