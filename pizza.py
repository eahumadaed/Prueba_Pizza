#pizza class

class Pizza:
    proteinicos = ['vacuno','pollo','carne vegetal'] #lista con proteinas
    vegetales = ['piña','tomate','champiñones','aceitunas'] #lista con vegetales
    t_masas = ['bordes de queso','delgada','tradicional'] #tipos de masa
    
    def __init__(self,proteina,vegetal_1,vegetal_2,t_masa):
        self.proteina = proteina
        self.vegetal_1 = vegetal_1
        self.vegetal_2 = vegetal_2
        self.t_masa = t_masa
        self.valida = False
        
    #metodos
    
    @staticmethod
    def validar_ingrediente(elemento, valores):
        return elemento in valores
    
    #pedido
    def pedido(self):
        print("\t******************************************")
        print("\t* ¡Gracias por llamar a Pizzería Panucci's! *")
        print("\t* ¿Qué ingredientes le gustaría para su   *")
        print("\t* pizza hoy?                              *")
        print("\t******************************************")
        #Solicito que ingrese los datos
        self.proteina = input("Ingrediente proteina: ")
        self.vegetal_1 = input("Ingrediente Vegetal 1: ")
        self.vegetal_2 = input("Ingrediente Vegetal 2: ")
        self.t_masa= input("Tipo de masa: ")
        
        #valido.
        
        self.valida = Pizza.validar_ingrediente(self.proteina,Pizza.proteinicos) \
            and Pizza.validar_ingrediente(self.vegetal_1,Pizza.vegetales) \
            and Pizza.validar_ingrediente(self.vegetal_2,Pizza.vegetales) \
            and Pizza.validar_ingrediente(self.t_masa,Pizza.t_masas)
        
