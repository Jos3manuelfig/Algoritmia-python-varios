documentos=[
'hola mengusta python',
'esto es uns pruba buena',
'quisiers aprender a programar',
'lo que sea como sea cuando'

]
resultado=[]
var=input('introduza plabra: ')
for doc in documentos:
    if var in doc:
        resultado.append(doc)
        print(f'{resultado}')
    else:
         print('No se encuentra')
         break