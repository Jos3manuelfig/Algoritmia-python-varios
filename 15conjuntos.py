lista1=['amarillo','azul','rojo','verde']
lista2=[ 'rojo', 'azul','blanco','gris']

conjunto1=set(lista1)
conjunto2=set(lista2)

resultado=conjunto1.difference(conjunto2)

resultado2=conjunto1.union(conjunto2)

resultado3=conjunto1.intersection(conjunto2)




print(resultado)
print(resultado2)
print(resultado3)

