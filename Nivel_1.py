##################
#### EJERCICIO 1 #####
# Instruccion: Crea crear_formateador(prefijo, fn_transformacion) que devuelva un closure. 
# La funcion devuelta debe procesar un texto aplicando la lambda/funcion fn_transformacion y concatenar el prefijo.

def crear_formateador(prefijo, fn_transformacion):
    return lambda texto: f"{prefijo}{fn_transformacion(texto)}"

fmt = crear_formateador("INFO: ", lambda t: t.upper())
print(fmt("sistema iniciado"))

##################
#### EJERCICIO 2 #####
# Instruccion: Crea crear_operador(factor, operacion_lambda) que devuelva un closure 
# capaz de aplicar la operacion recibida utilizando el factor encapsulado.

def crear_operador(factor, operacion_lambda):
    return lambda x: operacion_lambda(x, factor)

multiplicar_por_5 = crear_operador(5, lambda x, f: x * f)
print(multiplicar_por_5(10))
print(multiplicar_por_5(3))
print(multiplicar_por_5(7))


##################
#### EJERCICIO 3 #####
# Instruccion: Crea crear_descuento_dinamico(regla_condicional_lambda) que devuelva un closure. 
# Este evaluara el precio con la lambda enviada para determinar si aplica un descuento prefijado.

def crear_descuento_dinamico(regla_condicional_lambda):
    return lambda precio: precio * 0.8 if regla_condicional_lambda(precio) else precio

descuento_navidad = crear_descuento_dinamico(lambda p: p > 100)
print(descuento_navidad(150))
print(descuento_navidad(50))

##################
#### EJERCICIO 4 #####
# Instruccion: Crea crear_generador_sufijos(patron_lambda) que devuelva un closure 
# para transformar nombres de archivos basandose en una lambda de formato.

def crear_generador_sufijos(patron_lambda):
    return lambda nombre: f"{nombre}_{patron_lambda()}"

# Inyectamos una lambda con un valor fijo establecido por nosotros para evitar librerias externas
sufijo_version = crear_generador_sufijos(lambda: "v2_final")
print(sufijo_version("reporte_ventas"))

##################
#### EJERCICIO 5 #####
# Instruccion: Crea crear_conversor(tasa, margen_lambda) que retorne una funcion 
# para convertir montos calculando dinamicamente la comision adicional.

def crear_conversor(tasa, margen_lambda):
    return lambda monto: (monto * tasa) + margen_lambda(monto)

conversor_eur = crear_conversor(0.85, lambda m: m * 0.05)
print(conversor_eur(100))