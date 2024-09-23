# METODOS PARA TRABAJAR
#CON LISTAS
lista=[]
print(lista)
lista+=[1,2,3]
print(lista)
#___Agregar 1 Elemnto a la lista___
lista.append(4)
print(lista)
#___Agregar Varios Elementos
lista.extend([5,5,6,7])
print(lista)
#__Agregar Elemento y Posicion
lista.insert(1,9)
print(lista)
#__Consultar Elementos de la lista
print(lista[2])
#__consultar ultimo element
print(lista[-1])
#___Eliminar el ultimo Elemento
lista.pop()
print(lista)
lista.pop(5)
print(lista)

#__Eliminar el Valor Señalado
lista.remove(4)
print(lista)
#__comprobar valor en lista
print(33 in lista)
print(2 in lista)
#__consultar la Posicion enbque se encuentra un elmento en la lista
print(lista.index(2))
lista.extend([7,7,7])
print(lista)
#__consultar el total de veces que se repite un elemento ennuns lista
print(lista.count(7) )

#___ordenar lista (sort/sorted)
lista.sort()
lista.sort(reverse=True)
print(lista)
print(sorted(lista))

# longitud de una lista 
print(len(lista))

#___Consultar el Maxino y Minimo elemento de una lista 
print(max(lista))
print(min(lista))