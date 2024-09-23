def order(lista,orden):
    if orden == 'asc':
      for i in range(len(lista)):
            for j in range(i+1,len(lista)):
                if lista[i]>lista[j]:
                    lista[i],lista[j]=lista[j],lista[i]
    elif orden=='des':
        for i in range (len(lista)):
            for j in range(i+1,len(lista)):
                if lista[i]<lista[j]:
                    lista[i],lista[j]=lista[j],lista[i]
              
    return lista               
    
my_lista1=[4,7,5,2,10,67,1]
ordenarAsc=order(my_lista1,'asc')
print(ordenarAsc)

my_lista1=[4,7,5,2,10,67,1]
ordenarDes=order(my_lista1,'des')
print(ordenarDes)
                