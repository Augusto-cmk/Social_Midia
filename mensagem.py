import pickle

class Mensagem:
    def __init__(self) -> None:
        self.texto = None
    
    def set(self,object:object):
        self.texto = serialize(object)

    def get(self)->str:
        return self.texto


def serialize(classe:object):
    serialized_data = pickle.dumps(classe)
    return serialized_data
    
def deserialize(serialized_data):
    classe = pickle.loads(serialized_data)
    return classe