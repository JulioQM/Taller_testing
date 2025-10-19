import sentry_sdk ,logging

sentry_sdk.init(
    dsn="https://a345a9ba9e05130cb953750bb8cd92af@o4510210809790464.ingest.us.sentry.io/4510210811494400",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    #traces_sample_rate=1.0,
    send_default_pii=True,
)
def procesar_datos(lista):
    total = 0
    for valor in lista:
        total += valor
    return total / len(lista)
try:
    datos = [10, 20, 40]  ## error de tipo de dato sting -debe ser numero
#print(procesar_datos(datos))
except TypeError as e: ## modificacion de excepcion de error division para cero
    logging.error(f"Error detectado: {e}")
