def verificar_equilibrio(expresion):
    pila = []
    mapeo = {')': '(', '}': '{', ']': '['}

    for char in expresion:
        if char in '({[':
            pila.append(char)
        elif char in ')}]':
            if not pila or pila[-1] != mapeo[char]:
                return False
            pila.pop()

    return not pila

# Ejemplos de uso
expresion= "{[a * (c + d) - 5}"
if verificar_equilibrio(expresion)==True:
 
 print(f'La expresion {expresion} esta balanceada')
 
else:
     
     
     print('expresion no balanceda')

