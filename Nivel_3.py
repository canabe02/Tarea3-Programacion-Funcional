#####################
### Ejercicio 1 ##
# Crea la HOF procesar_coleccion(lista, fn_predicado, fn_transformacion) que combine 
# internamente filter y map pasando expresiones lambda.

def procesar_coleccion(lista, fn_predicado, fn_transformacion):
    return list(map(fn_transformacion, filter(fn_predicado, lista)))

print(procesar_coleccion([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0, lambda x: x ** 2))

#####################
### Ejercicio 2 ##
# Crea la HOF agrupar_por(lista, fn_clave) que reciba una colección de diccionarios 
# y los agrupe en un diccionario clave-valor basándose en el resultado de la lambda fn_clave.

def agrupar_por(lista, fn_clave):
    agrupado = {}
    for item in lista:
        clave = fn_clave(item)
        agrupado.setdefault(clave, []).append(item)
    return agrupado

usuarios = [{"rol": "admin", "id": 1}, {"rol": "user", "id": 2}, {"rol": "admin", "id": 3}]
print(agrupar_por(usuarios, lambda u: u["rol"]))

#####################
### Ejercicio 3 ##
# Crea ejecutar_y_rastrear(fn_tarea, n) que retorne un closure con el historial 
# de resultados de haber ejecutado fn_tarea n veces.

import random

def ejecutar_y_rastrear(fn_tarea, n):
    historial = [fn_tarea() for _ in range(n)]
    return lambda: historial

dado = ejecutar_y_rastrear(lambda: random.randint(1, 6), 3)
print(dado())


#####################
### Ejercicio 4 ##
# Crea la HOF componer_dos(f, g) que devuelva un closure que aplique f(g(x)), 
# permitiendo encadenar transformaciones complejas en línea.

def componer_dos(f, g):
    return lambda x: f(g(x))

componer = componer_dos(lambda x: x + 5, lambda x: x * 2)
print(componer(10))
print(componer(3))
print(componer(7))


#####################
### Ejercicio 5 ##
# Crea la HOF auditar_ejecucion(fn_objetivo, fn_logger) que mida el tiempo y envíe 
# el informe al closure/lambda de logging pasado por parámetro.

import time

def auditar_ejecucion(fn_objetivo, fn_logger):
    def envoltura(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = fn_objetivo(*args, **kwargs)
        tiempo = time.perf_counter() - inicio
        fn_logger(f"Tiempo de ejecución: {tiempo:.4f}s")
        return resultado
    return envoltura

def funcion_lenta():
    time.sleep(0.1)
    return "Fin de tarea"

auditada = auditar_ejecucion(funcion_lenta, lambda msg: print(f"LOG: {msg}"))
print(auditada())


