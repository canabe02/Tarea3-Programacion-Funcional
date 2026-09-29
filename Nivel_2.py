#################
## Ejercicio 1 ##
# Crea crear_contador_paso(fn_paso) que incremente su estado interno 
# utilizando una lambda fn_paso(cuenta_actual) en lugar de un incremento fijo.
def crear_contador_paso(fn_paso):
    cuenta = 0
    def incrementar():
        nonlocal cuenta
        cuenta += fn_paso(cuenta)
        return cuenta
    return incrementar

contador = crear_contador_paso(lambda c: 2 if c < 10 else 5)
print([contador(), contador(), contador()])

##################
# Ejercicio 2 ##
# Crea crear_acumulador_validado(criterio_lambda) que mantenga un total acumulado privado,
# pero solo sume los valores que superen la prueba de la lambda enviada.

def crear_acumulador_validado(criterio_lambda):
    total = 0
    def acumular(valor):
        nonlocal total
        if criterio_lambda(valor):
            total += valor
        return total
    return acumular

acumulador = crear_acumulador_validado(lambda v: v > 0)
print(acumulador(10))
print(acumulador(-5))
print(acumulador(20))


###################
## Ejercicio 3 ##
# Crea crear_promediador_filtrado(filtro_ruido_lambda) que acumule datos privadamente
# pero aplique la lambda para descartar valores atípicos antes de recalcular el promedio.
def crear_promediador_filtrado(filtro_ruido_lambda):
    suma = 0
    cantidad = 0
    def agregar_y_promediar(valor):
        nonlocal suma, cantidad
        if not filtro_ruido_lambda(valor):
            suma += valor
            cantidad += 1
        return suma / cantidad if cantidad > 0 else 0
    return agregar_y_promediar

promediador = crear_promediador_filtrado(lambda v: v > 100)
print(promediador(10))
print(promediador(20))
print(promediador(200))


####################
## Ejercicio 4 ##
# Crea crear_limitador_avanzado(max_intentos, fn_alerta) que cuente ejecuciones privadas
# y ejecute fn_alerta cuando el límite sea superado.
def crear_limitador_avanzado(max_intentos, fn_alerta):
    intentos = 0
    def ejecutar():
        nonlocal intentos
        intentos += 1
        if intentos > max_intentos:
            return fn_alerta(intentos)
        return f"Ejecución {intentos} exitosa"
    return ejecutar

limitador = crear_limitador_avanzado(2, lambda i: f"ALERTA: Bloqueado en intento {i}")
print(limitador())
print(limitador())
print(limitador())

#####################
### Ejercicio 5 ##
# Crea crear_conmutador(lista_estados) que alterne cíclicamente entre
# una lista de estados internos privados en cada llamada.
def crear_conmutador(lista_estados):
    indice = -1
    def alternar():
        nonlocal indice
        indice = (indice + 1) % len(lista_estados)
        return lista_estados[indice]
    return alternar

semaforo = crear_conmutador(["Verde", "Amarillo", "Rojo", "Rojo intermitente"])
print(semaforo())
print(semaforo())
print(semaforo())
print(semaforo())
print(semaforo()) ## Reinicio en verde