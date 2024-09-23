def minutos_segundos(segundos):
    m= segundos // 60
    s= segundos % 60
    return m, s
print('Convertir Minutos a Segundos')
seg= int(input('Intriduzca los Minutos: '))
min, segu = minutos_segundos(seg)

print(f'Equivalente es: {min} : {segu}')
    
    
    