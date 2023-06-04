import datetime
class controleUser:
    def __init__(self, data_nascimento, imagem) -> bool:
        paramentros = [self.__verificaData(data_nascimento), self.__verificaImagem(imagem)]
        return False not in paramentros

    def __verificaData(self, data:str):
        format = "%d/%m/%Y"
        try:
            return bool(datetime.strptime(data, format))
        except ValueError:
            return False

    def __verificaImagem(self, imagem:str):
        if imagem is None:
            return False
        else:
            return True