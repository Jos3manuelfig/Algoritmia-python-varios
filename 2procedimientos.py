def saludo(usuario):
    print(f'Hola que tal! {usuario}')
    
    
def main():
    nom= input('Introduzca su nombre :')
    saludo(nom)
    
    
if __name__== '__main__':
    main()