# Simulador de Búfer de Entrada en Python

## Descripción
Este proyecto es un simulador de un búfer de entrada implementado en Python. Utiliza un carácter especial (`eof`) como centinela para marcar el final de los datos, siguiendo el concepto de manejo de búferes y centinelas. Su objetivo es procesar eficientemente una lista de caracteres dividiéndolos en lexemas (palabras) y demostrando cómo manejar datos utilizando punteros.
![image](https://github.com/user-attachments/assets/298205a3-9919-4ffb-bc28-f7776729a3b9)

## Características
- Simulación de un búfer con tamaño fijo.
- Uso de punteros para manejar la entrada de datos.
- Manejo de un carácter centinela (`eof`) para indicar el final de los datos.
- Extracción y procesamiento de lexemas (fragmentos de texto entre espacios o delimitadores).

## Archivos Principales
1. **`buffer_simulator.py`**: Contiene la implementación del simulador de búfer.
2. **`README.md`**: Este archivo de documentación.

## Uso
### Entrada
La entrada es una lista de caracteres que representa un texto. Debe finalizar con el carácter especial `eof` para que el simulador detecte el final del texto.

### Ejecución
1. Define la lista de entrada como una cadena de texto.
2. Configura el tamaño del búfer (por defecto, 10 caracteres).
3. Llama a la función principal `simulador_buffer` con los parámetros definidos.

### Ejemplo
```python
entrada = list("Esto es un ejemplo de entrada con eof")
tamano_buffer = 10

simulador_buffer(entrada, tamano_buffer)
```

### Salida
El programa imprimirá los lexemas procesados:
```plaintext
Lexema procesado: Esto
Lexema procesado: es
Lexema procesado: un
Lexema procesado: ejemplo
Lexema procesado: de
Lexema procesado: entrada
Lexema procesado: con
Lexema procesado: eof
```

## Explicación del Código
El programa consta de tres funciones principales:

1. **`cargar_buffer(entrada, inicio, tamano_buffer)`**:
   - Llena el búfer con una sección de la entrada, comenzando desde el índice `inicio`.
   - Si la entrada tiene menos caracteres que el tamaño del búfer, agrega el carácter `eof`.

2. **`procesar_buffer(buffer)`**:
   - Itera sobre los caracteres del búfer para construir lexemas.
   - Los lexemas se delimitan por espacios o el carácter `eof`.
   - Imprime y devuelve los lexemas procesados.

3. **`simulador_buffer(entrada, tamano_buffer)`**:
   - Maneja la lógica del procesamiento iterativo.
   - Usa un puntero (`inicio`) para cargar el búfer en segmentos de tamaño fijo y procesarlos secuencialmente.

## Ventajas
- **Eficiencia**: Procesa datos en bloques fijos, optimizando el manejo de memoria.
- **Escalabilidad**: Puede adaptarse a flujos de entrada más grandes sin necesidad de leer todo el contenido en memoria.
- **Simplicidad**: La implementación modular facilita su comprensión y extensión.

## Comentario sobre el Código
```python
# Este programa simula el manejo de un búfer de entrada utilizando punteros y un centinela ("eof").
# Divide el texto en bloques de tamaño fijo, procesa cada bloque extrayendo lexemas
# delimitados por espacios y finaliza cuando se encuentra el carácter "eof".
# Este enfoque es ideal para simular el procesamiento eficiente de datos en tiempo real.
```

## Requisitos del Sistema
- Python 3.7 o superior.

## Ejecución del Programa
1. Clona el repositorio o copia el archivo `buffer_simulator.py`.
2. Ejecuta el script desde la línea de comandos:
   ```bash
   python buffer_simulator.py
   ```
## Contributions
https://github.com/Sofiamishel2003
https://github.com/DiegoDuaS
https://github.com/Maria-Villafuerte
https://github.com/Fabiola-cc
https://github.com/nicollegordillo

## Licencia
Este proyecto está disponible bajo la licencia MIT.

