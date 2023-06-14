class PersonService:
    def register_person(self, data_person):
        pass

    def refresh_perfil(self, id_person,data_person: dict):
        pass
    
    def id_person(self, email: str, password: str) -> int:
        pass
    
    def get_password_person(self,email)->str:
        pass
    
    def get_person(self, id):
        pass

    def get_friends_person(self, id_person):
        pass

    def get_post_friends_person(self, person_id):
        pass
    
    def get_len_colaborando(self, person_id):
        pass

    def get_len_colaborandores(self, person_id):
        pass

    def get_persons_all(self) -> list:
        pass
