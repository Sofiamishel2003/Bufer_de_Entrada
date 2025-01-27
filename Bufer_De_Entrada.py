# Simulador de búfer de entrada en Python
def cargar_buffer(entrada, inicio, tamano_buffer):
    """
    Carga el contenido del búfer desde la entrada.
    Si no hay suficientes datos para llenar el búfer, añade el centinela "eof".
    """
    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.append("eof")  # Añadir el centinela "eof" si faltan caracteres
    print(f"Búfer cargado: {buffer} (inicio: {inicio})")
    return buffer

def procesar_buffer(buffer, avance, lexema_actual):
    """
    Procesa el contenido del búfer y extrae lexemas.
    Un lexema está delimitado por espacios o el final del búfer.
    """
    lexemas_procesados = []

    while avance < len(buffer):
        char = buffer[avance]
        avance += 1

        if char.isspace() or char == "eof":
            if lexema_actual:  # Si hay un lexema acumulado, se procesa
                lexemas_procesados.append(lexema_actual)
                print(f"Lexema procesado: {lexema_actual}")
                lexema_actual = ""  # Reiniciar lexema actual
            if char == "eof":
                print("Fin del procesamiento: 'eof' encontrado.")
                break
        else:
            lexema_actual += char  # Acumular caracteres del lexema

    return lexemas_procesados, avance, lexema_actual

def simulador_buffer(entrada, tamano_buffer):
    """
    Simula el procesamiento de una entrada usando un búfer con tamaño fijo.
    Utiliza punteros de inicio y avance para manejar el procesamiento.
    """
    inicio = 0
    lexema_actual = ""  # Acumula caracteres entre espacios
    while inicio < len(entrada):
        # Cargar el búfer desde la posición actual del puntero inicio
        buffer = cargar_buffer(entrada, inicio, tamano_buffer)

        # Procesar el contenido del búfer
        avance = 0  # Puntero para avanzar dentro del búfer
        lexemas, avance, lexema_actual = procesar_buffer(buffer, avance, lexema_actual)

        # Avanzar el puntero de inicio al siguiente segmento
        inicio += tamano_buffer

        # Si el centinela "eof" fue encontrado, se termina el ciclo
        if "eof" in buffer:
            break

# Entrada de ejemplo
entrada = list("Esto es un ejemplo de entrada con eof")
tamano_buffer = 10
# Texto de entrada input
print("La entrada es: Esto es un ejemplo de entrada con eof")
# Ejecutar el simulador
simulador_buffer(entrada, tamano_buffer)