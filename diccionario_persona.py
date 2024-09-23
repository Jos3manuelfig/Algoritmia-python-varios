
persona={}
continuar=True
while continuar:
    clave=input('ingresa Clave: ')
    valor=input(clave+ ': ingrese valor: ')
    persona[clave]= valor
    print(persona)
    continuar=input('Deses Conituan s/n')== 's'