from src.calculator import suma, resta, division
from src.database import guardar_dato, obtener_dato

def ejecutar_flujo():
    print("Iniciando flujo de operaciones...")

    resultado = suma(5, 3)
    print(f"Suma: 5 + 3 = {resultado}")
    guardar_dato("suma_1", resultado)
    dato_guardado = obtener_dato("suma_1")
    print(f"Dato guardado recuperado: {dato_guardado}")

    print("Flujo de operaciones completado.")

if __name__ == "__main__":
    ejecutar_flujo()
