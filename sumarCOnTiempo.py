import random
import time

inten = 0
inicio = time.time()

for i in range(5):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    resul = num1 + num2
    
    resp = int(input(f'Cuánto es {num1} + {num2} : '))
    
    if resp == resul: 
        print('Has ganado')
        inten += 1
    else:
        print(f'Lo siento, has perdido. El resultado correcto es: {resul}')

tiempo_final = time.time() - inicio
print(f'Tu tiempo es de {tiempo_final:.2f} segundos')
print(f'Tus aciertos: {inten}')