def contar_palabras(palabras):
    
   encontrada={}
   for palabra in palabras.split():
       if palabra in encontrada:
           encontrada[palabra]+=1
       else:
           encontrada[palabra]=1
   return encontrada
   
texto= 'el sol el calor del sol el viento calor sol'

contar=contar_palabras(texto)
for palabra,cantidad in contar.items():
    print(palabra,cantidad)