def suma():
    try:
        num1= int(input('Numero1: '))
        num2=int(input('Numero2: '))
        resul= num1+ num2
        print(resul)
    except:
        print('solo puedes imgresear Numeros')
        
if __name__== '__main__':       
    suma()