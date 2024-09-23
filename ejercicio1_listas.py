import os

AGREGAR=1
INSERTAR=2
MOSTRAR=3
BUSCAR=4
ELIMINAR=5
ORDENAR=6
LIMPIAR=7
SALIR=0

frutas=[]

def imprimir_menu():
    os.system('clear')
    print(f'''                    Frutas
             {AGREGAR}) Agregar
             {INSERTAR}) Insertar
             {MOSTRAR}) Mostrar
             {BUSCAR}) Buscar
             {ELIMINAR}) Eliminar
             {ORDENAR}) Ordenar
             {LIMPIAR}) Limpiar
             {SALIR}) Salir''')

imprimir_menu()

def Agregar_registros():
     print( '                              Agregar')
     nom=input('Ingrese Nombre de Fruta: ')        
    fruta.append(nom) 
    print('Registro agregado con exito..!')        
    
    
def Insertar_Registros():
    print( '                              Insertar')
       nombre= input('ingresa una Fruta: ')
    pos= int(input('Ingresa una Posicion: '))
    frutas.insert(pos,nombre)
    print('Registro Insertado en la Posicion indicada')
    
    
def Mostrar_registro ():
       print( '                      Mostrar')
            if len(frutas )>0:
                print(frutas)
           else:
               print('No hay registros')
               
               
def Buscar_registro():
        print( '                       Buscar')
       
       

    