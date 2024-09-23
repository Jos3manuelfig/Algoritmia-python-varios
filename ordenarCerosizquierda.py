class Solution:
    def ordenar_ceros(self, lista: list):
        paso=0
        for i in range(len(lista)):
            if lista[i]!=0:
                lista[paso],lista[i]=lista[i],lista[paso]
                paso+=1
        return lista
        
        
my_lista=[1,2,0,3,4,0,5,6,0,7,0,8,9]

l1=Solution()
l1.ordenar_ceros(my_lista)
print(my_lista)