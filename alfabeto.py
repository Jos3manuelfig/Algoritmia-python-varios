

alfabeto= [chr(i) for i in range(97,123)]

vocal=['a','e','i','o','u']

print(alfabeto)

#lista2=[letra for letra in alfabeto if letra not vocal]

for letra in alfabeto:
        if letra not in vocal:
             
             print(" ( "+ letra , end= ')')
             
         