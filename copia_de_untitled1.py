# -*- coding: utf-8 -*-
"""Copia de Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wDhcylcYfEb0Q9SPFp7AElyTDNTB1n3i
"""

# variable para capturar la venta 
venta = float(input("¿cuanto fue el total de la compra? "))
# del calculo del IVA
iva = venta * 0.19
# suma el iva con la venta
total = venta + iva 
# visualiza el total a pagar por pantalla 
print("El IVA es = {:,.0f} y el total a pagar es = {:,.0f}".format(iva, total))
print(f"El IVA es = {iva:,.0f} y el total a pagar es = {total:,.0f}")

# variable para capturar la venta 
venta = float(input("cuanto fue el total de la compra?"))
# calculo del descuento
descuento = venta * 0.15
# resta el descuento con la venta
total = venta - descuento
# Visualiza el total a pagar por pantalla
print("El decuento es = {:,.0f} y el total a pagar es = {:,.0f}".format(descuento, total))
print(f"El descuento es = {descuento:,.0f} y el total a pagar es = {total:,.0f}")

#ventas del mes
venta1 = float(input("\ncual es el valor de la primera venta "))
venta2 = float(input("\ncual es el valor de la segunda venta "))
venta3 = float(input("\ncual es el valor de la tersera venta "))

#total ventas del mes 
suma = venta1+venta2+venta3
print(f"\nventas del mes {suma}")

#comision de 10% ventas 
comision = round((suma) * 0.10)
print(f"\ncomision del 10% {comision}  ")

# salario base 

print("\nsalario base $ 120000")

total = comision + 1200000 

print(f"\nsalario base mas comision  {total}")

# variable para capturar total estudiantes
totalestudiantes = float(input("cual es el total de estudiantes"))
# variable para capturar hombres
hombres = float(input("hombres"))
# variable para capturar hombres
mujeres = float(input("mujeres"))
# calculo porcentajeh
porcentajeh = hombres * 100 / totalestudiantes
# calculo porcentajem
porcentajem = mujeres * 100 / totalestudiantes
# visualizar el porcentaje de hombres y mujeres en pantalla
print("El porcentajeh es = {:,.0f} y el porcentajem es = {:,.0f}".format(porcentajeh,porcentajem))
print(f"El porcentajeh es = {porcentajeh:,.0f} y el porcentajem es = {porcentajem:,.0f}")

"""Taller 2:

Dando continuidad con la primera entrega del proyecto, en esta oportunidad el estudiante debe realizar las siguientes validaciones utilizando la sentencia condicional IF.

Si el empleado es mayor de 55 años disfrutará de un bono de prepensión correspondiente al 5% de su sueldo básico.

Si el empleado es casado y tiene hijos se le otorgará un paseo cada diciembre

Si el sueldo básico está entre 1000000 y 1500000 tendrá una comisión del 2% sobre el valor del sueldo; Si el sueldo básico está entre 1500001 y 2000000 tendrá una comisión del 5% sobre el valor del sueldo; para todos los demás casos no habrá comisión.

Si el empleado trabajó más de 20 días al mes y su sueldo es menor a 1000000 tendrá derecho a un bono de alimentación.

"""

#Variable de tipo Entero que almacena el numero de cédula de una persona
Id = input ("Digite su número de cédula : ")
Identificacion = "No de identificacion : "
#Variable de tipo String que almacena los nombres de una persona
Nombre = input("Digite sus nombres : ")
Nombrecom = "Nombre completo : "
#Variable de tipo String que almacena los apellidos de una persona
Apellidos = input("Digite sus apellidos : ")
#Variable de tipo String que almacen la dirección de residencia de una persona
Di = input("Digite su dirección de residencia : ")
Dir = "Dirección : "
#Variable de tipo Entero que almacena el número de teléfono de una persona
Telefono = input("Digite su número telefónico : ")
Tel = "Teléfono : "
#Variable de tipo Entero que almacena la edad de una persona
Edad = int(input("Digite su edad : "))
Eda = "Edad : "
#Variable de tipo String que almacena el estado civil de una persona
Estado = str(input("Digite su estado civil : "))
Estad = "Estado Civil : "
#Variable de tipo Entero que almacena el número de hijos de una persona
Hi = int(input("Digite número de hijos : "))
Hij = "Numero de Hijos : "
#Variable de tipo Entero que almacena la estatura de una persona
Estatuta = input("Digite su estatura : ")
Estatur = "Estatura : "
#Variable de tipo Entero que almacena la fecha de contratacion de una persona
Dia = input("Digite fecha de contratación : Día : ")
Mes = input("Mes : ")
An = input("Año : ")
Contratacio = "Fecha de Contratación : "
#Variable de tipo Entero que almacena el sueldo básico de una persona
Sueldo = int(input("Digite su sueldo básico : "))
Sueldoba = "Sueldo Básico : $"
#Variable de tipo Entero que almacena los días laborados de una persona
diasla = int(input("Digite los dias laborados : "))
Laborados = "Dias Laborados : "
if Edad > 55:
  bono = Sueldo * 0.05
  print(Sueldo, Sueldoba)
  print(f"El empleado se hace acreedor a un bono del 5% correspondiente a ${bono:,.0f}")
if Sueldo >=1000000 and Su <= 1500000:
    comis = Sueldo * 0.02
    sueldo = Sueldo + comis
    print(f"Recibe una comision de ${comis:,.0f} que corresponde al 2% de ${Su:,.0f} para un total de sueldo de ${sueldo:,.0f}")
if Sueldo >1500000 and Su <=2000000:
    comis = Sueldo * 0.05
    sueldo = Sueldo + comis
    print(f"Recibe una comision de ${comis:,.0f} que corresponde al 5% de ${Su:,.0f} para un total de sueldo de ${sueldo:,.0f}")
else:
  print(Suedo, Sueldoba)
#4. Si el empleado trabajó más de 20 días al mes y su sueldo es menor a 1000000 tendrá derecho a un bono de alimentación.
if diasla > 20 and Sueldo < 1000000:
  print(diasla, Laborados)

  print(f"El empleado trabajo mas de 20 dias y su sueldo es menor a $1.000.000 tiene derecho a un bono de alimentacion")
else:
  print(diasla, Laborados)

"""Se necesita un sistema que despliega una tabla de
multiplicar de un número dado por el usuario. ciclo for
"""

num = int(input("Digite el número de la tabla de multiplicar: "))

for i in range(11):
  print(i , " x ", num , " = ", i * num)

"""Se necesita un sistema que pida un sueldo de un
trabajador, si el sueldo es mayor a 655000, no tedrá
ninguna bonificación, pero si es menor tiene bonificación
del 4%. Al final se desea saber el total del sueldo con
o sin bonificación. Preguntar si desea ejecutar de nuevo
el programa con el ciclo while.
"""

resp = "si"
while  resp == "si":
    sueldo = float(input("cual es tu salario: "))
    if  sueldo <= 655000: 
        bono = sueldo * 0.04 
        total = sueldo + bono
        input(f"Su sueldo es:${sueldo} mas bonificacion de:${bono:,.1f} total a pagar es:$ {total}")
       # resp = input("¡¿Desea iniciar otra ves?")
    else:            
        input(f" Su sueldo a pagar es:${sueldo} y no tienes bonificacion este mes  ")      
    resp = input("¡¿Desea iniciar otra ves?: ")

"""Un maestro necesita un sistema para capturar las
calificaciones de 5 parciales de sus alumnos, después
recapturarlas necesita que se despliegue el promedio,
cuando ya no quiera capturar más alumnos, necesita que
se despliegue el promedio general de todos los alumnos
capturados. Preguntar si desea ejecutar de nuevo el
programa con el ciclo while.

"""

resp = "si"
while resp == "si" or resp == "s":
  cal1 = float(input("Digite la calificación 1: "))
  cal2 = float(input("Digite la calificación 2: "))
  cal3 = float(input("Digite la calificación 3: "))
  cal4 = float(input("digite la calificacion 4: "))
  cal5 = float(input("Digite la calificación 5: "))
  prom = round((cal1 + cal2 + cal3 + cal4 + cal5)/ 5)

  if prom >= 3.0:
    estado = "Aprobado"
  else:
    estado = "Reprobado"
  print(f"El promedio es= {prom} y el estado es = {estado}")
  resp = input("¿Desea Cácular otras 5 calificaciones? ")

"""Crear un bucle que cuente todos los números pares hasta
el 100 ciclo for

"""

for i in range(0,101,2):
  print(i)

"""Haz una tabla de multiplicar utilizando el ciclo for
ciclo for
"""

num = int(input("Digite los numeros de la tabla de multiplicar: "))

for p in range(21):
  print(p , " x ", num , " = ", p * num)

"""Escribir un programa que pregunte al usuario su edad y
muestre por pantalla todos los años que ha cumplido
(desde 1 hasta su edad). ciclo for
"""

edad = int(input("Cuantos años tienes: "))

for i in range(edad):
    input(i)