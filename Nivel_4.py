#####################
### Ejercicio 1 ##
# Crea crear_validador_múltiple(*lambdas_criterios) que retorne un closure que 
# evalúe si un objeto cumple todas las reglas pasadas como argumento.

def crear_validador_multiple(*lambdas_criterios):
    return lambda objeto: all(criterio(objeto) for criterio in lambdas_criterios)

validador_pass = crear_validador_multiple(lambda s: len(s) > 5, lambda s: any(c.isdigit() for c in s))
print(validador_pass("contra12"))
print(validador_pass("hola"))

#####################
### Ejercicio 2 ##
# Crea la HOF memoizar_avanzado(fn_costosa, max_items) que retorne un closure 
# controlando el estado privado de una memoria caché con límite de capacidad.

def memoizar_avanzado(fn_costosa, max_items):
    cache = {}
    orden = []
    
    def envoltura(arg):
        if arg in cache:
            return cache[arg]
        
        resultado = fn_costosa(arg)
        
        if len(cache) >= max_items:
            viejo_arg = orden.pop(0)
            del cache[viejo_arg]
            
        cache[arg] = resultado
        orden.append(arg)
        return resultado
        
    return envoltura

cache_limitado = memoizar_avanzado(lambda x: x * 2, max_items=2)
print(cache_limitado(10))
print(cache_limitado(20))
print(cache_limitado(30))  # El límite elimina la primera entrada calculada

#####################
### Ejercicio 3 ##
# Crea crear_pipeline(*funciones_transformacion) que permita pasar un dato inicial 
# y hacerlo fluir en orden a través de todas las lambdas/funciones del pipeline.

def crear_pipeline(*funciones_transformacion):
    def ejecutar(dato_inicial):
        resultado = dato_inicial
        for funcion in funciones_transformacion:
            resultado = funcion(resultado)
        return resultado
    return ejecutar

pipe = crear_pipeline(lambda x: x.strip(), lambda x: x.upper(), lambda x: f"[{x}]")
print(pipe("  hola mundo  "))

#####################
### Ejercicio 4 ##
# Crea crear_sistema_eventos() que devuelva un closure gestor capaz de registrar 
# suscriptores (lambdas) y emitir eventos notificando a cada uno.

def crear_sistema_eventos():
    suscriptores = []
    
    def gestor(accion, payload=None):
        if accion == "suscribir":
            suscriptores.append(payload)
        elif accion == "emitir":
            for sub in suscriptores:
                sub(payload)
                
    return gestor

eventos = crear_sistema_eventos()
eventos("suscribir", lambda msg: print(f"Subscriptor recibió: {msg}"))
eventos("emitir", "Actualización disponible")

#####################
### Ejercicio 5 ##
# Crea crear_consultor(campo) que devuelva una HOF para generar filtros dinámicos 
# sobre listas de diccionarios/objetos mediante expresiones lambda complejas.

def crear_consultor(campo):
    return lambda lista, condicion_lambda: list(filter(lambda obj: condicion_lambda(obj.get(campo)), lista))

db = [{"nombre": "Ana", "edad": 25}, {"nombre": "Luis", "edad": 30}]
query_edad = crear_consultor("edad")
print(query_edad(db, lambda e: e >= 30))