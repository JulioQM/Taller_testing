import sentry_sdk

sentry_sdk.init(
    #Token propio
)

def procesar_datos(lista):
    total = 0
    for valor in lista:
        total += valor
    return total / len(lista)

datos = [10, "20", 40]
print(procesar_datos(datos))