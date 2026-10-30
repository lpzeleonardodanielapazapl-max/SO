
# Práctica 1 - Hilos y Sincronización


Al iniciar el programa se crean 24 documentos,
cada uno tiene un identificador único y un tamaño
simulado entre 1 y 5.

Los documentos se almacenan en una cola compartida.

Se van a crear 4 hilos que los vamos a notar o identicar  como
Trabajador-1, Trabajador-2, Trabajador-3 y Trabajador-4.

Cada trabajador va a obtener documentos de la cola y
simula su procesamiento mediante time.sleep().

Los documentos completados se registran en un
diccionario compartido mediante el Lock.

Al finalizar, se muestra la cantidad 
procesados por cada trabajador.

--Interpretación de los trabajadores

-Trabajador-1

Retira los documentos de la cola y registra aquellos
que logra procesar. La cantidad  puede variar
según la ejecución de los demás hilos aun que lo esperado sea que todos los hilos(trabajadores) trabajen con una misma cantidad.

-Trabajador-2

Trabaja sobre la misma cola compartida.
No procesa documentos que hayan sido retirados antes  por otro trabajador.

-Trabajador-3

Procesa documentos de forma concurrente con
los demás trabajadores, respetando el mecanismo
de sincronización para actualizar los resultados.

-Trabajador-4

Continúa retirando documentos disponibles y
finaliza cuando la cola queda vacía.

--Interpretación

Los cuatro trabajadores comparten los 24 documentos.

La cantidad procesada por cada uno puede cambiar
entre ejecuciones porque el sistema operativo
planifica los hilos y los documentos requieren
diferentes tiempos de procesamiento.

La suma de los documentos debe ser 24 y ningún
identificador puede repetirse.

--Evidencias de ejecución
La evidencias se lograran ver de mejor manera en la carpeta de capturas, donde se encuantra cada ejecucion realizada(4).


--  Preguntas

--¿Por qué queue.Queue es apropiada para compartir trabajos?

Porque es una cola segura para trabajar con varios
hilos. nos permite que los trabajadores puedan sacar 
documentos sin que dos hilos obtengan el mismo o se repitan cada
elemento de la cola.

--¿Qué protege Lock y qué pasaría si se actualizara el resumen sin él?

Lock protege la actualización del diccionario
compartido de resultados.

Sin Lock, las operaciones concurrentes sobre
datos compartidos podrían causar condiciones
de carrera si no se realizan de forma segura.

--¿Qué cambiarías si cada documento tuviera que guardarse en un archivo real?

Se agregaría una operación de escritura de archivos,
con nombres únicos para cada documento.

También se manejarían errores de lectura y escritura
y se protegerían los recursos compartidos cuando
fuera necesario.
