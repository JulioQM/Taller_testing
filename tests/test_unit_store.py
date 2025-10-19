from src.database import guardar_dato, obtener_dato, db

def test_guardar():
    db.clear()
    guardar_dato("suma_1", 5)
    assert 'suma_1' in db
    assert db['suma_1'] == 5

def test_obtener():
    db.clear()
    guardar_dato("suma_1", 5)
    resultado = obtener_dato("suma_1")
    assert resultado == 5
    assert obtener_dato("resta") is None
