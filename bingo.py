import random



def bingo():
    
    intentos = 0
    num= random.randint(1,5)
    print("*****ADIVINA EL NUMERO SECRETO****")
    a=0
    while intentos < 5:
        a =int(input("ingresa un numero : ")
        intentos+=1
        if a>num:
            print("El Número ingresado Es MAYOR al secreto ")
        if a < num:
            print("El Número ingresado Es MENOR al secreto")
        if a ==num:              
            print(f"FELICIDADES HAS GANADO. en {intentos} intentos")
            break
      
        if intentos == 5:
            
            print("\n")
            print("\n")
            
            print("lo siento has perdido era el número 15")   
            os.system('cls')  
         
bingo()

 
     
     
     

        
    

