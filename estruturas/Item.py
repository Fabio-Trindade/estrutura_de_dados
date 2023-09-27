class Item:
    def __init__(self, chave : int):
        self._chave = chave
    
    @property
    def chave(self):
        return self._chave