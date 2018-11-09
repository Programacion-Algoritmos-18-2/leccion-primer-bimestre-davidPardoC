#Importar Modulo
from mipaquete.modelo import *
#Crea Empleado
e=Empleado()
e.agregar_nombre("luis")
e.agregar_apellido("Benitez")
e.agregar_cedula("1110001")
print(e.presentar_datos())

print("\nEmpleado Por Horas:\n")

#Crea Empleado por horas
e1=EmpleadoPorHoras()
nombre=input("Ingrese el nomnre: ")
e1.agregar_nombre(nombre)
e1.agregar_apellido("Andrade")
e1.agregar_cedula("112233")
e1.agregar_numero_horas(20.2)
e1.agregar_valor_hora(15)
print(e1.presentar_datos())

print("\nEmpleado Fijo\n")
#Crea Empleado Fijo
e2=EmpleadoFijo()
e2.agregar_sueldo_fijo(3002)
e2.agregar_descuento(10)
e2.agregar_cedula("112233")
comision=input("Comision: ")
comision=int(comision)
e2.agregar_comision(comision)
e2.agregar_nombre("Ana")
e2.agregar_apellido("Diaz")
print(e2.presentar_datos())

print("\n EMpleado SEmanal\n")
#Crea Empleado Semnanal
e3=EmpleadoSemanal()
e3.agregar_nombre("David")
e3.agregar_apellido("Pardo")
e3.agregar_cedula("1111")
e3.agregar_numero_semanas(4)
e3.agregar_valor_semana(100)
e3.agregar_comision(300)
print(e3.presentar_datos())