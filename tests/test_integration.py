from src.calculator import suma
from src.database import guardar_dato, obtener_dato


def test_opracion_almacenamiento():
    resultado_suma = suma(10, 5)
    guardar_dato("suma_10_5", resultado_suma)
    dato_recuperado = obtener_dato("suma_10_5")
    assert dato_recuperado == 15