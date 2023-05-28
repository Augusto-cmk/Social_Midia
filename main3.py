from src.services.person_status_service import PersonStatusService
from src.services.person_service import PersonService
from src.services.friend_service import FriendService
from src.services.post_service import PostService
from src.services.message_service import MessageService

# PersonService().insert_person(
#     {
#         "name":"Pedro Maia",
#         "photo": "",
#         "email": "",
#         "password": "",
#         "state":"",
#         "city":"",
#         "birthday":"18/12/2000"
#     }
# )

# PersonService().insert_person(
#     {
#         "name":"Victória Rodrigues",
#         "photo": "",
#         "email": "",
#         "password": "",
#         "state":"",
#         "city":"",
#         "birthday":"28/07/1999"
#     }
# )

# Pedro id = 1
# Vic id = 2

# MessageService().send_message(1,2,"Opa, eae linda ?")

# print(MessageService().get_messages(1,2))

datas = [{'texto':"opa","date":"12/10/2023"},{'texto':"opa","date":"12/10/2022"},{'texto':"opa","date":"12/10/2021"}]

print(sorted(datas,key=lambda x: x['date']))