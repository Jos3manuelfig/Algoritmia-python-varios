mylista1= list(range(1,100))
mylista2=list(range(1,100,2))

for i in mylista2:
    mylista1.remove(i)
print(mylista1)
print('\n')
listaN=[x for x in mylista1 if x not in mylista2]
    
print(listaN)
