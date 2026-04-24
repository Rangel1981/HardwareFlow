from abc import abstractmethod, ABC

class Dispositivo(ABC):
    def __init__(self, marca, modelo, valor_base_reparo):
        self.marca = marca
        self.modelo = modelo
        self.valor_base_reparo = valor_base_reparo

    def __str__(self):
        return f"O Dispositivel da marca{self.marca} e do modelo{self.modelo} tem o valor de {self.valor_base_reparo}"

    @abstractmethod
    def calcular_reparo(self):
        pass

class Computador(Dispositivo):
    def __init__(self, marca, modelo, tipo, valor_base_reparo):
        super().__init__(marca, modelo, valor_base_reparo)
        self.tipo = tipo

    def calcular_reparo(self):
        if self.tipo == "Desktop":
            taxa = 50.0
       
        else:
            taxa = 100.0

        return self.valor_base_reparo + taxa
    
class Smartphone(Dispositivo):
    def __init__(self, marca, modelo, valor_base_reparo):
        super().__init__(marca, modelo, valor_base_reparo)
        self.tela_trincada = False

    def calcular_reparo(self):
        taxa_celular = 0.0
        if self.tela_trincada == True:
            taxa_celular = 70.0
        
        return self.valor_base_reparo + taxa_celular