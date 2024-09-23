from datetime import datetime

fecha= datetime.now()
print('Fecha :',fecha.strftime('%d/%m/%Y '))
print('Hora  : ',fecha.strftime('  %H : %M'))

def main():
    
    
   def Invertir_cadena():
        #Forma 1:
        cadena="Paralelepipedo"
        print(cadena[::-1])
        
        #Forma2
        Ncadena=""
       
        for i in cadena:
            Ncadena=i+Ncadena
        print(Ncadena)
        #Forma 3
        CadenaN=reversed(cadena)
        print("".join(CadenaN))
       
       #Forma 4
        for char in range(len(cadena)-1 ,-1,-1):
           
            print(cadena[char], end='')
       
        
            
   Invertir_cadena()
    
if __name__== '__main__':
     main()