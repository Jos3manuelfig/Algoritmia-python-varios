from typing import Union

class Comando:
    def ejecutar(self):
        raise NotImplementedError("Debes implementar el método ejecutar.")

class Combatiente:
    def atacar(self, enemigo):
        print(f"El combatiente ataca a {enemigo} con una espada.")

class Mago:
    def atacar(self, enemigo):
        print(f"El mago ataca a {enemigo} con un hechizo.")

class AtacarEnemigo(Comando):
    def __init__(self, personaje: Union[Combatiente, Mago], enemigo: str) -> None:
        self._personaje = personaje
        self._enemigo = enemigo

    def ejecutar(self) -> None:
        self._personaje.atacar(self._enemigo)

# Ejemplo de uso
combatiente = Combatiente()
mago = Mago()

comando_combatiente = AtacarEnemigo(combatiente, "dragón")
comando_mago = AtacarEnemigo(mago, "troll")

comando_combatiente.ejecutar()  # El combatiente ataca a dragón con una espada.
comando_mago.ejecutar()         # El mago ataca a troll con un hechizo.