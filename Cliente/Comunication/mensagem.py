import pickle
import netifaces

def serialize(classe:object):
    serialized_data = pickle.dumps(classe)
    return serialized_data
    
def deserialize(serialized_data):
    classe = pickle.loads(serialized_data)
    return classe

def fragment_msg(mensagem,size_required):
    fragmentos = []
    tamanho_mensagem = len(mensagem)
    tamanho_fragmento = size_required

    for i in range(0, tamanho_mensagem, tamanho_fragmento):
        fragmento = mensagem[i:i+tamanho_fragmento]
        fragmentos.append(fragmento)
    
    return fragmentos

def obter_ip_interface():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        if interface != 'lo':  # Ignorar interface loopback
            enderecos = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in enderecos:
                endereco_ip = enderecos[netifaces.AF_INET][0]['addr']
                return endereco_ip