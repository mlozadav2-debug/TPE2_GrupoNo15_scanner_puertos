# MANUAL DE USO - Escáner de Puertos TCP

## 1. Propósito

Este manual explica cómo ejecutar y utilizar el escáner de puertos TCP desarrollado en Python para la práctica de Seguridad Informática.

## 2. Requisitos

- Computadora con Python 3 instalado.
- Visual Studio Code u otro editor de código.
- Archivo `scanner_puertos.py`.
- Terminal en macOS o PowerShell/Terminal en Windows.

La biblioteca `socket` forma parte de la biblioteca estándar de Python y no requiere una instalación adicional.

## 3. Verificar Python

### macOS

```bash
python3 --version
```

### Windows

```powershell
py --version
```

Evidencia en Windows:

![Python instalado](imagenes/03_windows_python_version.png)

## 4. Iniciar la aplicación

### macOS

```bash
python3 scanner_puertos.py
```

### Windows

```powershell
py scanner_puertos.py
```

El programa solicitará:

1. Dirección IP.
2. Puerto inicial.
3. Puerto final.

## 5. Prueba de puerto abierto

Para realizar una prueba controlada se puede levantar un servidor HTTP local en el puerto 8000.

### macOS

```bash
python3 -m http.server 8000
```

### Windows

```powershell
py -m http.server 8000
```

En Windows se observa el servidor funcionando:

![Servidor local en el puerto 8000](imagenes/04_windows_servidor_8000.png)

Luego se ejecuta el escáner con:

```text
IP: 127.0.0.1
Puerto inicial: 7995
Puerto final: 8005
```

El resultado esperado es que el puerto 8000 aparezca como **ABIERTO**.

Resultado en macOS:

![Resultado en macOS](imagenes/01_mac_resultado_puerto_8000.png)

Resultado en Windows:

![Resultado en Windows](imagenes/05_windows_resultado_abierto.png)

## 6. Prueba de puerto cerrado

Para comprobar el comportamiento ante un puerto cerrado, se detiene el servidor con `Ctrl + C`.

![Servidor detenido](imagenes/06_windows_servidor_detenido.png)

Después se ejecuta nuevamente el escáner con:

```text
IP: 127.0.0.1
Puerto inicial: 8000
Puerto final: 8000
```

El resultado debe indicar:

```text
Puertos analizados: 1
Puertos abiertos: 0
No se encontraron puertos abiertos.
```

![Prueba con puerto cerrado](imagenes/07_windows_resultado_cerrado.png)

## 7. Interpretación de resultados

- **Puerto ABIERTO:** existe un servicio escuchando y aceptando conexiones TCP en ese puerto.
- **No se encontraron puertos abiertos:** dentro del rango analizado no se detectaron servicios accesibles.
- **Error de rango:** el programa valida que los puertos estén entre 1 y 65535 y que el puerto inicial no sea mayor que el final.

## 8. Recomendaciones

- Utilizar solamente direcciones IP de equipos propios, máquinas virtuales o laboratorios autorizados.
- No realizar escaneos sobre redes, servidores o dispositivos ajenos sin autorización.
- Detener el servidor de prueba cuando la práctica haya terminado.
