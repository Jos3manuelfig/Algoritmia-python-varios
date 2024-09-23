import random
import string
import os
letras='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros='0123456789'
simbolos='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'



def generador(n: int):
    os.system('clear')
    pwTotal=numeros+simbolos+numeros
    pw=''
    for i in range(n):
        pw+=random.choice(pwTotal)
    return pw + 'tuti'
if __name__== '__main__':
       
    nuevo= generador(20)
    print(nuevo)
    
    