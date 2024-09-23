my_lista=[x for x in range(101)]
print(my_lista)
print('\n')
pares=list(filter(lambda x: x%2==0,my_lista))
print(pares)