class CommentService:
    def __init__(self):
        super().__init__()

    def insert_comment(self, post_id: int, person_id: int, text: str) -> bool:
        pass
    
    def get_comment(self, id_comment: int) -> dict:
        pass
