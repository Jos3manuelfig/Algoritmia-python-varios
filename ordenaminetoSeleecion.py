#ordenaminetonpor seleccionb
def ordenamientoSeleccion(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]<lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista 


my_lista=[4,78,5,2,10,67]
print(ordenamientoSeleccion(my_lista))

