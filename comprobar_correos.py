correos=[
'manuel@gmai.com',
'jose@yahoo.com',
'ana@hotmail.com',
'mandsrina'

]

for n in correos:
   if '@' in n:
        print(f'{n} es validos')
   else:
         print(f' {n} es invalido*')