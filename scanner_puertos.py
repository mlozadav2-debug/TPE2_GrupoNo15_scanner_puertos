import socket

print("=" * 45)
print("        ESCÁNER DE PUERTOS TCP")
print("=" * 45)

ip = input("Ingrese la dirección IP: ")

try:
    puerto_inicial = int(input("Ingrese el puerto inicial: "))
    puerto_final = int(input("Ingrese el puerto final: "))

    if puerto_inicial < 1 or puerto_final > 65535:
        print("Error: los puertos deben estar entre 1 y 65535.")
        raise SystemExit

    if puerto_inicial > puerto_final:
        print("Error: el puerto inicial no puede ser mayor al puerto final.")
        raise SystemExit

except ValueError:
    print("Error: debe ingresar números válidos.")
    raise SystemExit

puertos_abiertos = []

print("\nEscaneando...")
print(f"IP: {ip}")
print(f"Rango: {puerto_inicial} - {puerto_final}")
print("-" * 45)

for puerto in range(puerto_inicial, puerto_final + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    resultado = sock.connect_ex((ip, puerto))

    if resultado == 0:
        print(f"Puerto {puerto} - ABIERTO")
        puertos_abiertos.append(puerto)

    sock.close()

total_analizados = puerto_final - puerto_inicial + 1

print("\n" + "=" * 45)
print("RESUMEN DEL ESCANEO")
print("=" * 45)

print(f"IP analizada: {ip}")
print(f"Puertos analizados: {total_analizados}")
print(f"Puertos abiertos: {len(puertos_abiertos)}")

if puertos_abiertos:
    print("Lista de puertos abiertos:", puertos_abiertos)
else:
    print("No se encontraron puertos abiertos.")

print("=" * 45)
