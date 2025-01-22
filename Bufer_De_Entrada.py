# Simulador de búfer de entrada en Python
def cargar_buffer(entrada, inicio, tamano_buffer):
    """
    Carga el contenido del búfer desde la entrada.
    Si no hay suficientes datos para llenar el búfer, añade el centinela "eof".
    """
    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.append("eof")
    return buffer

def procesar_buffer(buffer):
    """
    Procesa el contenido del búfer y extrae lexemas.
    Un lexema está delimitado por espacios o el final del búfer.
    """
    lexema = ""
    lexemas_procesados = []

    for char in buffer:
        if char.isspace() or char == "eof":
            if lexema:
                lexemas_procesados.append(lexema)
                print(f"Lexema procesado: {lexema}")
                lexema = ""
            if char == "eof":
                break
        else:
            lexema += char

    return lexemas_procesados

def simulador_buffer(entrada, tamano_buffer):
    """
    Simula el procesamiento de una entrada usando un búfer con tamaño fijo.
    Utiliza punteros de inicio y avance para manejar el procesamiento.
    """
    inicio = 0
    while inicio < len(entrada):
        # Carga el búfer con los datos a partir de "inicio"
        buffer = cargar_buffer(entrada, inicio, tamano_buffer)

        # Procesa el contenido del búfer
        procesar_buffer(buffer)

        # Avanza el puntero de inicio al siguiente segmento
        inicio += tamano_buffer

# Entrada de ejemplo
entrada = list("Esto es un ejemplo de entrada con eof")
tamano_buffer = 10
# Texto de entrada input
print("La entrada es: Esto es un ejemplo de entrada con eof")
# Ejecutar el simulador
simulador_buffer(entrada, tamano_buffer)