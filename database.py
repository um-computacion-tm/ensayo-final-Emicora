from dispositivo import Dispositivo

class Database:

    def __init__(self, data: dict= None) -> None:
        lista = data.get('dispositivos',[])
        self.database = []
        for i in lista:
            self.database.append(Dispositivo(diccionario=i))


    def delete_by_id(self, id):
        for i in self.database:
            if (i.id == id):
                self.database.remove(i)

    def add_dispositivo(self, disp4= None, diccionario= None):
        if disp4: 
            self.database.append(disp4)
        if diccionario:
            self.database.append(Dispositivo(diccionario=diccionario))


