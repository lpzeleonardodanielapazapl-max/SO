
import threading
import queue
import time
import random

trabajos = queue.Queue()
resultados = {}
lock = threading.Lock()

for doc_id in range(1, 25):
    trabajos.put((doc_id, random.randint(1, 5)))

def trabajador(nombre):
    while True:
        try:
            doc_id, tamano = trabajos.get_nowait()
        except queue.Empty:
            break

        time.sleep(tamano * 0.1)

        with lock:
            resultados[nombre] += 1
            print(f"{nombre} procesó el documento {doc_id}")


hilos = []

for i in range(1, 5):
    nombre = f"Trabajador-{i}"
    resultados[nombre] = 0

    hilo = threading.Thread(
        target=trabajador,
        args=(nombre,)
    )
    hilos.append(hilo)


for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

print("\n===== RESUMEN =====")

total = 0

for nombre, cantidad in resultados.items():
    print(f"{nombre}: {cantidad} documentos")
    total += cantidad

print(f"\nTotal de documentos procesados: {total}")

if total == 24:
    print("Todos los documentos fueron procesados correctamente.")
else:
    print("Error: faltan documentos por procesar.")
