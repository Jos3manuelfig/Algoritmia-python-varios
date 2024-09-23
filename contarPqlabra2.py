def contarPalabra(texto):
    texto=texto.lower()
    palabras=texto.split()
    encontrada={}
    for palabra in palabras:
        if palabra in encontrada:
            encontrada[palabra]+=1
        else:
            encontrada[palabra]=1
    return encontrada
    
texto1='las palabras las cosas palabras mejores cosas '  
 
print(texto1)    
             
frecuencia =contarPalabra(texto1)
print(frecuencia)


for i,j in frecuencia.items():
    print(i,j)