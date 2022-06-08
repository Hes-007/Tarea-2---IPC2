from Nodos import Nodo

class ListaCircularDoblementeEnlazada:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacio(self):
        if self.primero == None:
            return True
        else:
            return False 

    def AgregarInicio(self, numero):
        if self.vacio():
            self.primero = self.ultimo = Nodo(numero)
        else:
            aux = Nodo(numero)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__unir_nodos__()

    def AgregarFinal(self, numero):
        if self.vacio():
            self.primero = self.ultimo = Nodo(numero) 
        else:
            aux1 = self.ultimo
            self.ultimo = aux1.siguiente = Nodo(numero)
            self.ultimo.anterior = aux1
        self.__unir_nodos__()

    def __unir_nodos__(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero

    def RecorrerInicioFin(self):
        aux = self.primero
        while aux:
            print(aux.numero)
            aux = aux.siguiente
            if aux == self.primero:
                break


    def RecorrerFinInicio(self):
        aux1 = self.ultimo
        while aux1:
            print(aux1.numero)
            aux1 = aux1.anterior
            if aux1 == self.ultimo:
                break

    def buscar(self, numero):
        aux = self.ultimo
        while aux:
            if aux.numero == numero:
                print("anterior: ", aux.siguiente.numero)
                print("actual: ", aux.numero)
                print("siguiente: ", aux.anterior.numero)
            
            if aux.siguiente == self.ultimo:
                return
            aux = aux.siguiente
                
            
            

