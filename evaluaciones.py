#class pizza test
from pizza import Pizza

#imprimo las listas
print("Proteinas ",Pizza.proteinicos)
print("Vegetales ",Pizza.vegetales)
print("Masas ",Pizza.t_masas)


#Valido la una lista
lista_ingredientes = ['salsa de tomate', 'salsa bbq']
print("Prueba pizza Valida: ",Pizza.validar_ingrediente("salsa de tomate", lista_ingredientes))

#instancia

Pizza_pedido = Pizza("piña","pollo", "tomate", "tradicional")
Pizza_pedido.pedido()


#muestro en pantalla lo que selecciono el Usuario

print(f"Mi ingredientes vegetales son: {Pizza_pedido.vegetal_1} y {Pizza_pedido.vegetal_2}")
print(f"Mi ingrediente proteico es: {Pizza_pedido.proteina}")
print(f"Mi tipo de masa es: {Pizza_pedido.t_masas}")
print(f"¿Mi pizza es valida? {'SI' if Pizza_pedido.valida else 'NO'}")
