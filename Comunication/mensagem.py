import pickle


def serialize(classe:object):
    serialized_data = pickle.dumps(classe)
    return serialized_data
    
def deserialize(serialized_data):
    classe = pickle.loads(serialized_data)
    return classe