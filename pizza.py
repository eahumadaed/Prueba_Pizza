#pizza class

class Pizza:
    proteinicos = ['vacuno','pollo','carne vegetal'] #lista con proteinas
    vegetales = ['piña','tomate','champiñones','aceitunas'] #lista con vegetales
    t_masas = ['bordes de queso','delgada','tradicional']
    
    def __init__(self,proteina,vegetal_1,vegetal_2,t_masa):
        self.proteina = proteina
        self.vegetal_1 = vegetal_1
        self.vegetal_2 = vegetal_2
        self.t_masa = t_masa
        self.valida = False
        
    #metodos
    
    @staticmethod
    def validar_ingredientes(elemento, valores):
        return elemento in valores
    
    def pedido(self):
        #Solicito que ingrese los datos
        self.proteina = input("Ingrediente proteina")
        self.vegetal_1 = input("Ingrediente Vegetal 1")
        self.vegetal_2 = input("Ingrediente Vegetal 2")
        self.t_masa= input("Tipo de masa")
        
        #valido.
        
        self.valida = validar_ingredientes(self.proteina,Pizza.proteinicos) \
            and validar_ingredientes(self.vegetal_1,Pizza.vegetales) \
            and validar_ingredientes(self.vegetal_2,Pizza.vegetales) \
            and validar_ingredientes(self.t_masa,Pizza.t_masas)
        
