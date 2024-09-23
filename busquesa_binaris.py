def buscarValor(lista,valor):
    izq= 0
    der=len(lista)-1
    while izq< der:
        medio = (izq + der)//2
        if lista[medio]== valor:
            return medio
        elif lista[medio] < valor:
            izq= valor +1
        else:
            der= valor-1
            
        return -1
           
     lista=[1,4,7,67,87,99,100,105,300]      
     valorBuscado =100
                
 resul=buscarValor(lista, valorBuscado)
 
 if resul != -1
     print('El valor buscado es:', valorBuscado, 'en la posicion', resul)
  else:
      print('el calpr buscado', valorBuscado, 'No se encuentra en la lisra')
            