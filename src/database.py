db = {}

def guardar_dato(operacion, respuesta):
    db[operacion] = respuesta

def obtener_dato(operacion):
    return db.get(operacion, None)