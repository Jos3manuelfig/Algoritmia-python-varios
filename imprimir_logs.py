import time

def imprimir_logs():
    tiempo_inicial = time.time()
    while True:
        tiempo_actual = time.time()
        if tiempo_actual - tiempo_inicial >= 10:
            break
        print(f"Registro a los {tiempo_actual - tiempo_inicial:.2f} segundos")
        time.sleep(2)

imprimir_logs()
