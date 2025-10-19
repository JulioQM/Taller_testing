"""
Este programa contiene errores simples de lógica y ejecución.
El objetivo es detectar, registrar, corregir y documentar cada incidencia.
"""

import logging

logging.basicConfig(
    filename="app.log",                    # Guarda los logs en un archivo (opcional)
    level=logging.INFO,                    # Nivel mínimo que se mostrará
    format="%(asctime)s - %(levelname)s - %(message)s",  # Formato del mensaje
    datefmt="%Y-%m-%d %H:%M:%S"            # Formato de la fecha/hora
)


""" logging.info("Inicio del proceso")
logging.warning("Archivo no encontrado, usando ruta alternativa")
logging.error("No se pudo conectar a la base de datos") """


def dividir(a, b):
    try:
        resultado = a / b
        logging.info(f"División realizada: {a} / {b} = {resultado}")
        return resultado
    except ZeroDivisionError as e:
        logging.error(f"Error de división: {e}")
        return None

def promedio(lista_numeros):
    """Calcula el promedio de una lista de números."""
    try:
        total = 0
        for n in lista_numeros:
            total += n
        return total / len(lista_numeros)  
    except ZeroDivisionError as e:
        logging.error(f"Error de divion:{e}")
        return None

def obtener_elemento(lista, indice):
    """Devuelve un elemento de la lista según el índice indicado."""
    return lista[indice] 

def calcular_total(precios):
    """Suma los precios de una lista."""
    try:
        total = 0
        for p in precios:
            total += p
        return total  
    except ZeroDivisionError as e:
        logging.error(f"Error de divion:{e}")
        return None

# ------------------------------------------------------
# FUNCIÓN PRINCIPAL
# ------------------------------------------------------

def main():
    logging.info("Inicio del programa")

    resultado_div = dividir(10, 1)
    print("Resultado de la división:", resultado_div)

    datos = [1,2]
    print("Promedio:", promedio(datos))

    lista = [1, 2, 3]
    print("Elemento:", obtener_elemento(lista, 2)) # corregido

    
    precios = [10, 20, 30, 40] ## coloca numeros enteros
    print("Total de precios:", calcular_total(precios))

    logging.info("Fin del programa")

if __name__ == "__main__":
    main()
