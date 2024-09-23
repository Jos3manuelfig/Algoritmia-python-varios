import time
import threading

class Cronometro:
    def __init__(self):
        self.start_time = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.perf_counter()
            self.running = True
            print("Cronómetro iniciado...")
            threading.Thread(target=self._update_display).start()

    def stop(self):
        if self.running:
            elapsed_time = time.perf_counter() - self.start_time
            self.running = False
            print(f"Cronómetro detenido. Tiempo transcurrido: {int(elapsed_time * 1_000_000)} µs")

    def _update_display(self):
        while self.running:
            elapsed_time = time.perf_counter() - self.start_time
            print(f"\rTiempo transcurrido: {elapsed_time:.6f} s", end="")
            time.sleep(0.1)

def main():
    cronometro = Cronometro()
    while True:
        command = input("\nIngrese 'start' para iniciar el cronómetro o 'stop' para detenerlo: ").strip().lower()
        if command == 'start':
            cronometro.start()
        elif command == 'stop':
            cronometro.stop()
            break
        else:
            print("Comando no reconocido. Por favor, ingrese 'start' o 'stop'.")

if __name__ == "__main__":
    main()