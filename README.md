
---

# **Simulador de Búfer de Entrada en Python**

Este proyecto es un simulador de un búfer de entrada con tamaño fijo en Python. El objetivo principal es procesar datos eficientemente utilizando un concepto de búfer, punteros (`inicio` y `avance`), y un carácter especial (`eof`) como centinela para indicar el final de los datos.

## **Características del Simulador**
- Procesa datos de entrada utilizando un búfer con un tamaño fijo (10 caracteres por defecto).
- Extrae "lexemas" (secuencias de caracteres entre espacios o al final del texto).
- Maneja espacios y un carácter especial `eof` para delimitar el final del procesamiento.
- Utiliza punteros para organizar el manejo del búfer y recargar datos cuando se alcanza el final del segmento actual.

---

## **Cómo Funciona**
El programa está dividido en tres funciones principales:

### 1. **`cargar_buffer(entrada, inicio, tamano_buffer)`**
Carga un segmento del texto en un búfer con tamaño fijo.
- Si el segmento es más pequeño que el tamaño del búfer, se agrega el centinela `eof`.
- Esta función asegura que siempre haya datos disponibles para procesar en un tamaño predefinido.

### 2. **`procesar_buffer(buffer, avance, lexema_actual)`**
Procesa el contenido del búfer y extrae lexemas.
- Identifica lexemas delimitados por espacios o el carácter `eof`.
- Maneja un acumulador (`lexema_actual`) para procesar lexemas que puedan estar divididos entre dos búferes consecutivos.

### 3. **`simulador_buffer(entrada, tamano_buffer)`**
Controla el flujo general del programa.
- Divide la entrada en segmentos utilizando `cargar_buffer`.
- Procesa cada segmento con `procesar_buffer`.
- Utiliza punteros (`inicio` y `avance`) para manejar el progreso a lo largo de la entrada.

---

## **Requisitos**
- Python 3.6 o superior.

---

## **Ejemplo de Uso**
Entrada: 
```plaintext
Esto es un ejemplo de entrada con eof
```

Tamaño del búfer: `10`

Salida esperada:
```plaintext
La entrada es: Esto es un ejemplo de entrada con eof
Lexema procesado: Esto
Lexema procesado: es
Lexema procesado: un
Lexema procesado: ejemplo
Lexema procesado: de
Lexema procesado: entrada
Lexema procesado: con
Lexema procesado: eof
```

---

## **Cómo Ejecutarlo**
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/simulador-buffer-python.git
   cd simulador-buffer-python
   ```

2. Ejecuta el archivo principal:
   ```bash
   python bufer_simulador.py
   ```

---

---

## **Ventajas del Proyecto**
- **Eficiencia**: Procesa datos en fragmentos de tamaño fijo, optimizando el uso de memoria.
- **Modularidad**: Cada función tiene una responsabilidad clara, facilitando la extensibilidad.
- **Flexibilidad**: Fácilmente adaptable para manejar otros tamaños de búfer o diferentes delimitadores.

---

## Contributions
https://github.com/Sofiamishel2003
https://github.com/DiegoDuaS
https://github.com/Maria-Villafuerte
https://github.com/Fabiola-cc
https://github.com/nicollegordillo

## Licencia
Este proyecto está disponible bajo la licencia MIT.

